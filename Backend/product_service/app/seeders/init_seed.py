from app.models.category_model import Category
from app.models.product_model import Product
from app.shared.database import engine, SessionLocal, Base

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Category).count() == 0:
        categories = [
            Category(name="Electrónica"),
            Category(name="Ropa"),
            Category(name="Libros")
        ]
        db.add_all(categories)
        db.commit()
        print("✅ Categorías creadas.")

        db.refresh(categories[0])
        db.refresh(categories[1])
        db.refresh(categories[2])

        productos = [
            Product(name="Laptop X1", description="Portátil de alto rendimiento", photo_url="", size="15'", weight="2kg", unit_price=1500, iva=19.0, category_id=categories[0].id),
            Product(name="Auriculares Bluetooth", description="Sonido envolvente", photo_url="", size="N/A", weight="200g", unit_price=120, iva=19.0, category_id=categories[0].id),
            Product(name="Smartwatch S3", description="Reloj inteligente con GPS", photo_url="", size="42mm", weight="100g", unit_price=220, iva=19.0, category_id=categories[0].id),

            Product(name="Camisa Formal", description="Camisa de algodón", photo_url="", size="M", weight="300g", unit_price=35, iva=10.0, category_id=categories[1].id),
            Product(name="Jeans Slim", description="Pantalón denim ajustado", photo_url="", size="32", weight="700g", unit_price=45, iva=10.0, category_id=categories[1].id),
            Product(name="Chaqueta Impermeable", description="Ideal para lluvia", photo_url="", size="L", weight="900g", unit_price=80, iva=10.0, category_id=categories[1].id),

            Product(name="Clean Code", description="Libro de Robert C. Martin", photo_url="", size="N/A", weight="500g", unit_price=40, iva=5.0, category_id=categories[2].id),
            Product(name="El Principito", description="Novela corta clásica", photo_url="", size="N/A", weight="200g", unit_price=15, iva=5.0, category_id=categories[2].id),
            Product(name="1984", description="Distopía de Orwell", photo_url="", size="N/A", weight="300g", unit_price=22, iva=5.0, category_id=categories[2].id),
        ]

        db.add_all(productos)
        db.commit()
        print("✅ Productos creados.")
    else:
        print("⚠️ Las categorías ya existen. No se creó nada nuevo.")

    db.close()

if __name__ == "__main__":
    init_db()
