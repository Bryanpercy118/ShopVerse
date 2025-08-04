from sqlalchemy.orm import Session
from app.models.order_model import Order, OrderItem
from app.schemas.order_schema import OrderCreate
from fastapi import HTTPException

def create_order(db: Session, user_id: int, data: OrderCreate):
    if not data.items:
        raise HTTPException(status_code=400, detail="La orden debe contener al menos un producto.")

    # Calcular el total
    total = sum((item.unit_price + (item.iva or 0)) * item.quantity for item in data.items)

    # Crear orden principal
    order = Order(user_id=user_id, total=total, status="pendiente")
    db.add(order)
    db.commit()
    db.refresh(order)

    # Agregar los ítems de la orden
    for item in data.items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=item.unit_price,
            iva=item.iva
        )
        db.add(order_item)

    db.commit()
    db.refresh(order)
    return order

def get_user_orders(db: Session, user_id: int):
    return db.query(Order).filter(Order.user_id == user_id).all()

def get_order_by_id(db: Session, order_id: int, user_id: int):
    return db.query(Order).filter_by(id=order_id, user_id=user_id).first()

def get_all_orders(db: Session):
    return db.query(Order).all()

def update_order_status(db: Session, order_id: int, new_status: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return None
    order.status = new_status
    db.commit()
    db.refresh(order)
    return order

def get_status_counts(db: Session):
    from sqlalchemy import func
    results = db.query(Order.status, func.count(Order.id)).group_by(Order.status).all()
    return {status: count for status, count in results}

def get_revenue_by_status(db: Session):
    from sqlalchemy import func
    results = db.query(Order.status, func.sum(Order.total)).group_by(Order.status).all()
    return {status: float(total or 0) for status, total in results}

def get_all_orders(db: Session):
    return db.query(Order).all()
