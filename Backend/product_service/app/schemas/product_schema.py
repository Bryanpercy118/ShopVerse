from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    photo_url: Optional[str]
    size: Optional[str]
    weight: Optional[str]
    unit_price: float
    iva: float
    category_id: Optional[int]

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
