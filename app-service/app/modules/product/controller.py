from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.modules.product.schemas import CreateProductRequest, CreateProductResponse, ProductSchema
from app.modules.product.service import create_product ,get_products

router = APIRouter()

@router.post("/", response_model=CreateProductResponse)
async def post_create_product(payload: CreateProductRequest, db: AsyncSession=Depends(get_db)):
    return await create_product(payload, db)

@router.get("/", response_model=list[ProductSchema])
async def get_products_data(db: AsyncSession=Depends(get_db)):
    return await get_products(db)
