from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user_model import User
from app.schemas.auth_schema import LoginRequest, RegisterRequest
from app.services.auth_service import (
    verify_password,
    create_access_token,
    hash_password
)
from app.shared.database import get_db

def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        print("Usuario no encontrado:", data.email)
        raise HTTPException(status_code=401, detail="Usuario no encontrado.")

    if not verify_password(data.password, user.password):
        print("Contraseña incorrecta")
        raise HTTPException(status_code=401, detail="Contraseña incorrecta.")

    try:
        # Convertimos el role a str explícitamente
        token = create_access_token({
            "sub": str(user.id),
            "email": user.email,
            "role": str(user.role)  # <- solución clave aquí
        })
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except Exception as e:
        print("Error generando token:", e)
        raise HTTPException(status_code=500, detail="Error generando token.")


def register_customer(data: RegisterRequest, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")

    new_user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role="customer"  # si tu modelo usa Enum, asegúrate que acepte string
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token = create_access_token({
            "sub": str(new_user.id),
            "email": new_user.email,
            "role": str(new_user.role)
        })

        return {
            "message": "Usuario registrado correctamente",
            "access_token": token,
            "token_type": "bearer"
        }
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al registrar el usuario.")

def logout_user():
    return {"message": "Sesión cerrada. Elimina el token en el cliente."}
