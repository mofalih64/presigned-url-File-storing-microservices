from fastapi import APIRouter
from app.modules.storage.controller import router as storage_router

api_router = APIRouter()
api_router.include_router(storage_router, prefix="/storage", tags=["Storage"])
