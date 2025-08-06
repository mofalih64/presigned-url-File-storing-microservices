import os
from uuid import uuid4
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.token import decode_token
from app.modules.storage.models import File as FileModel
from app.core.config import settings
from app.utils.exceptions import bad_request, not_found
from sqlalchemy import select

async def handle_file_upload(token: str, file: UploadFile, db: AsyncSession):
    # Decode and validate token
    meta = decode_token(token)
    print(meta)
    print(file)

    # Validate uploaded file matches the token claims
    if file.content_type != meta.get("mime_type"):
        raise bad_request("File MIME type does not match token payload")

    content = await file.read()
    if len(content) != meta.get("size"):
        raise bad_request("File size does not match token payload")

    if file.filename != meta.get("filename"):
        raise bad_request("Filename does not match token payload")

    # Store file
    ext = file.filename.split(".")[-1]
    unique_filename = f"{uuid4().hex}.{ext}"
    save_path = os.path.join(settings.STATIC_DIR, unique_filename)

    os.makedirs(settings.STATIC_DIR, exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(content)

    file_url = f"{settings.BASE_URL}/static/{unique_filename}"

    # Save metadata to DB
    new_file = FileModel(
        name=file.filename,
        size=len(content),
        mime_type=file.content_type,
        url=file_url
    )

    db.add(new_file)
    await db.commit()
    await db.refresh(new_file)

    return {
        "success": True,
        "file_id": new_file.id,
        "url": file_url
    }

async def get_image(file_id: str, db: AsyncSession):
    result = await db.execute(select(FileModel).where(FileModel.id == file_id))
    print(result)
    print(file_id)
    file = result.scalars().first()
    print(file)

    if not file:
        raise not_found("File not found")
    
    return file    

    
    