from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.modules.product.repository import create_product_record
from app.modules.product.schemas import CreateProductRequest, CreateProductResponse

async def create_product(
    payload: CreateProductRequest,
    db: AsyncSession
) -> CreateProductResponse:
    # (Optional) validate image_id with storage service

    product = await create_product_record(db, payload.name, payload.price, payload.image_id)

    return CreateProductResponse(success=True, message="Product created", product=product)
