from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth_schema import LoginRequest, RegisterRequest
from app.controllers import auth_controllers
from app.shared.database import get_db

router = APIRouter()


@router.post("/login", tags=["Auth"])
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return auth_controllers.login_user(data, db)


@router.post("/register", tags=["Auth"])
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return auth_controllers.register_customer(data, db)


@router.post("/logout", tags=["Auth"])
def logout():
    return auth_controllers.logout_user()
