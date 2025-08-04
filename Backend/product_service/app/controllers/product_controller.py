from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product_schema import ProductCreate, Product
from app.services import product_service
from app.shared.database import SessionLocal

# Dependency para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> Product:
    return product_service.create_product(db, product)

def get_products(db: Session = Depends(get_db)) -> list[Product]:
    return product_service.get_products(db)

def get_product(product_id: int, db: Session = Depends(get_db)) -> Product:
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

def update_product(product_id: int, product_data: ProductCreate, db: Session = Depends(get_db)) -> Product:
    updated = product_service.update_product(db, product_id, product_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated

def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = product_service.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}

def internal_get_product(product_id: int, db: Session = Depends(get_db)) -> Product:
    product = product_service.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product
