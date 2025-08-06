from pydantic import BaseModel

class FileMeta(BaseModel):
    filename: str
    size: int
    mime_type: str

class PresignedUrlResponse(BaseModel):
    upload_url: str
