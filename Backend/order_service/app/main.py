from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import order_routes
from app.shared.database import create_db_and_tables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(order_routes.router)
