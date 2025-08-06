from fastapi import APIRouter
from app.modules.storage.controller import router as storage_router
from app.modules.product.controller import router as product_router

api_router = APIRouter()
api_router.include_router(storage_router, prefix="/storage", tags=["Storage"])
api_router.include_router(product_router, prefix="/product", tags=["Product"])
