from sqlalchemy import Column, Float, String, DateTime
from app.core.database import Base
import uuid
from datetime import datetime
from sqlalchemy import func
def get_id():
    return str(uuid.uuid4())


class File(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True, index=True, default=get_id)
    name = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    mime_type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
