from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    iva: Optional[float] = 0

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class OrderItemOut(OrderItemCreate):
    id: int
    order_id: int

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: int
    user_id: int
    total: float
    status: str
    created_at: datetime  
    items: List[OrderItemOut]

    class Config:
        orm_mode = True

class OrderStatusUpdate(BaseModel):
    status: str
