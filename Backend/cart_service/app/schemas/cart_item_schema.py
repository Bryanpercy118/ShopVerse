from pydantic import BaseModel
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int
    quantity: int


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    quantity: int


class CartItemOut(CartItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class EnrichedCartItem(BaseModel):
    id: int
    product_id: int
    quantity: int
    name: str
    unit_price: float
    total_price: float

    class Config:
        orm_mode = True
