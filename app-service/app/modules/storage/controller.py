from fastapi import APIRouter, HTTPException
from app.modules.storage.schemas import FileMeta, PresignedUrlResponse
from app.modules.storage.service import generate_presigned_url

router = APIRouter()

@router.post("/upload-url", response_model=PresignedUrlResponse)
async def get_upload_url(file_meta: FileMeta):
    return generate_presigned_url(file_meta)
