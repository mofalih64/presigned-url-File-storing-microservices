from fastapi import APIRouter
from app.modules.storage.schemas import FileResponse
from app.modules.storage.service import handle_file_upload
from app.core.database import get_db
from app.core.database import AsyncSession
from fastapi import Query, File, UploadFile, Depends
from app.modules.storage.service import get_image
router = APIRouter()

@router.post("")
async def upload_file(
    token: str = Query(...),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    return await handle_file_upload(token=token, file=file, db=db)

@router.get("{file_id}", response_model=FileResponse)
async def get_image_data(file_id: str, db: AsyncSession = Depends(get_db)):
    return await get_image(file_id, db)
