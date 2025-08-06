from pydantic import BaseModel

class CreateProductRequest(BaseModel):
    name: str
    price: float
    image_id: str


class ImageData(BaseModel):
    id: str
    name: str
    url: str

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    image_id: str
    image_data : ImageData | None = None

    model_config = {
        "from_attributes": True,
        "use_enum_values": True
    }


class CreateProductResponse(BaseModel):
    success: bool
    message: str
    product: ProductSchema


