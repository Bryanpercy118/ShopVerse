from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.cart_item_schema import CartItemOut, CartItemCreate, CartItemUpdate, EnrichedCartItem
from app.shared.database import SessionLocal
from app.shared.jwt_bearer import get_current_user_id
from app.services import cart_service

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_cart(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return cart_service.get_cart_items(db, user_id)

def add_item(data: CartItemCreate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return cart_service.add_to_cart(db, user_id, data)

def update_item(item_id: int, data: CartItemUpdate, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return cart_service.update_cart_item(db, user_id, item_id, data)

def delete_item(item_id: int, user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    return cart_service.delete_cart_item(db, user_id, item_id)

def get_cart_details(user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)) -> list[EnrichedCartItem]:
    return cart_service.get_cart_with_details(db, user_id)