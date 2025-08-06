from pydantic import BaseModel

class CreateProductRequest(BaseModel):
    name: str
    price: float
    image_id: str

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    image_id: str

    model_config = {
        "from_attributes": True,
        "use_enum_values": True
    }


class CreateProductResponse(BaseModel):
    success: bool
    message: str
    product: ProductSchema


