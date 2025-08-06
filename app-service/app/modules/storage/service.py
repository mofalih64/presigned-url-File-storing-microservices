from app.modules.storage.schemas import FileMeta, PresignedUrlResponse
from app.utils.token import generate_token
from app.core.config import settings
from app.utils.exceptions import bad_request

# Define allowed MIME types and max size in bytes
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def generate_presigned_url(file_meta: FileMeta) -> PresignedUrlResponse:
    if file_meta.mime_type not in ALLOWED_MIME_TYPES:
        raise bad_request("Invalid file type")
    if file_meta.size > MAX_FILE_SIZE:
        raise bad_request("File size exceeds limit")
    if file_meta.size <= 0:
        raise bad_request("File size must be greater than 0")
    token = generate_token({
        "filename": file_meta.filename,
        "size": file_meta.size,
        "mime_type": file_meta.mime_type,
    })

    upload_url = f"{settings.storage_service_url}/storage?token={token}"
    return PresignedUrlResponse(upload_url=upload_url)
