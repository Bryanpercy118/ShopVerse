from sqlalchemy.orm import Session
from app.models.cart_item_model import CartItem
from app.schemas.cart_item_schema import CartItemCreate, CartItemUpdate, EnrichedCartItem
from app.shared.http_client import get_product_by_id

def get_cart(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def get_cart_items(db: Session, user_id: int):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()

def get_cart_with_details(db: Session, user_id: int) -> list[EnrichedCartItem]:
    cart_items = db.query(CartItem).filter(CartItem.user_id == user_id).all()
    enriched = []

    for item in cart_items:
        product = get_product_by_id(item.product_id)
        if not product:
            continue  # O manejar error según se prefiera

        enriched.append(EnrichedCartItem(
            id=item.id,
            product_id=item.product_id,
            quantity=item.quantity,
            name=product.get("name", ""),
            unit_price=product.get("unit_price", 0.0),
            total_price=round(product.get("unit_price", 0.0) * item.quantity, 2)
        ))

    return enriched

def add_to_cart(db: Session, user_id: int, item: CartItemCreate):
    cart_item = db.query(CartItem).filter_by(user_id=user_id, product_id=item.product_id).first()
    if cart_item:
        cart_item.quantity += item.quantity
    else:
        cart_item = CartItem(user_id=user_id, **item.dict())
        db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

def update_cart_item(db: Session, user_id: int, item_id: int, data: CartItemUpdate):
    item = db.query(CartItem).filter_by(id=item_id, user_id=user_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item no encontrado")

    update_data = data.dict(exclude_unset=True) 
    for key, value in update_data.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


def delete_cart_item(db: Session, item_id: int, user_id: int):
    item = db.query(CartItem).filter_by(id=item_id, user_id=user_id).first()
    if item:
        db.delete(item)
        db.commit()
    return item
