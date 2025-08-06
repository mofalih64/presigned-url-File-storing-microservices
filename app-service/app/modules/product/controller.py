from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.modules.product.schemas import CreateProductRequest, CreateProductResponse
from app.modules.product.service import create_product

router = APIRouter()

@router.post("/", response_model=CreateProductResponse)
async def post_create_product(payload: CreateProductRequest, db: AsyncSession=Depends(get_db)):
    return await create_product(payload, db)
