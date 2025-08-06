from sqlalchemy import Column, Float, String, Integer
from app.core.database import Base
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_id = Column(String, nullable=False)
