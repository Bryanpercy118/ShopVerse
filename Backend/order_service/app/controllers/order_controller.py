from fastapi import Depends, HTTPException
from fastapi import Body  # <- necesario si no usas Pydantic como parámetro directamente
from sqlalchemy.orm import Session
from app.services import order_service
from app.schemas.order_schema import OrderCreate, OrderOut
from app.shared.database import SessionLocal
from app.shared.jwt_bearer import get_current_user_id
from app.schemas.order_schema import OrderStatusUpdate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_order(
    data: OrderCreate = Body(...), 
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    return order_service.create_order(db, user_id, data)

def user_orders(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    return order_service.get_user_orders(db, user_id)

def order_detail(
    order_id: int,
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    order = order_service.get_order_by_id(db, order_id, user_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return order

def admin_orders(db: Session = Depends(get_db)):
    return order_service.get_all_orders(db)


def get_order_status_stats(db: Session = Depends(get_db)):
    return order_service.get_status_counts(db)

def get_order_revenue_by_status(db: Session = Depends(get_db)):
    return order_service.get_revenue_by_status(db)


def admin_orders(db: Session = Depends(get_db)):
    return order_service.get_all_orders(db)