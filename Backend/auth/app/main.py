from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes
from app.shared.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth")

@app.get("/")
def root():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Conexión a la base de datos exitosa."}
    except SQLAlchemyError as e:
        return {"status": "error", "message": f"Error en la conexión: {str(e)}"}
    finally:
        db.close()
