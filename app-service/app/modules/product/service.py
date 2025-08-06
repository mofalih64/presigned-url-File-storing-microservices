from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.product.repository import create_product_record
from app.modules.product.schemas import CreateProductRequest, CreateProductResponse, ProductSchema
from app.core.config import settings
import httpx
from fastapi import HTTPException
from app.modules.product.models import Product
from sqlalchemy import select
async def create_product(
    payload: CreateProductRequest,
    db: AsyncSession
) -> CreateProductResponse:
    # (Optional) validate image_id with storage service
    await check_image_id(payload.image_id)
    product = await create_product_record(db, payload.name, payload.price, payload.image_id)

    return CreateProductResponse(success=True, message="Product created", product=product)

async def get_products(db: AsyncSession)->list[ProductSchema]:
    products=await db.execute(select(Product).order_by(Product.id.desc()))
    products=products.scalars().all()
    #  add image data for each product, should groupd the products ids in array and call the storage service once
    for product in products:
        product.image_data = await check_image_id(product.image_id,False)

    return products

async def check_image_id(image_id: str,raise_if_not_found=True):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{settings.storage_service_url}/storage{image_id}")
            response.raise_for_status()  # Raises HTTPStatusError for 4xx/5xx
            return response.json()
        except httpx.HTTPStatusError as e:
            if(raise_if_not_found):
                if e.response.status_code == 404:
                    raise HTTPException(status_code=400, detail="Image not found in storage service")
                raise HTTPException(status_code=500, detail="Failed to validate image ID")
            return None
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Storage service unreachable")
