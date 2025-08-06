from sqlalchemy.ext.asyncio import AsyncSession
from app.modules.product.models import Product

async def create_product_record(db: AsyncSession, name: str, price: float, image_id: str):
    product = Product(name=name, price=price, image_id=image_id)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product
