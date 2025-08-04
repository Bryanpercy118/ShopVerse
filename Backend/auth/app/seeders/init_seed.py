from app.models.user_model import Base, User
from app.shared.database import engine, SessionLocal
from app.services.auth_service import hash_password

def init_db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    if not db.query(User).filter_by(email="admin@demo.com").first():
        user = User(
            name="Admin",
            email="admin@demo.com",
            password=hash_password("123456"),
            role="admin"
        )
        db.add(user)
        db.commit()
        print("Usuario admin creado.")
    else:
        print("Usuario admin ya existe.")
    db.close()

if __name__ == "__main__":
    init_db()
