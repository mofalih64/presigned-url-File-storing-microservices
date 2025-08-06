from pydantic import BaseModel

class FileMeta(BaseModel):
    name: str
    size: int
    mime_type: str
    id: str

class FileResponse(FileMeta):
    url: str
