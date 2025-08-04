from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.category_schema import CategoryCreate, Category
from app.services import category_service
from app.shared.database import SessionLocal

# Dependency para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_category(category: CategoryCreate, db: Session = Depends(get_db)) -> Category:
    return category_service.create_category(db, category)

def get_categories(db: Session = Depends(get_db)) -> list[Category]:
    return category_service.get_categories(db)

def get_category(category_id: int, db: Session = Depends(get_db)) -> Category:
    category = category_service.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

def update_category(category_id: int, data: CategoryCreate, db: Session = Depends(get_db)) -> Category:
    updated = category_service.update_category(db, category_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return updated

def delete_category(category_id: int, db: Session = Depends(get_db)):
    deleted = category_service.delete_category(db, category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"message": "Categoría eliminada exitosamente"}
