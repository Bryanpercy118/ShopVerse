from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.product_routes import router as product_routes
from app.routes.category_routes import router as category_routes
from app.routes.internal_product_routes import router as internal_router
from app.shared.database import create_db_and_tables

app = FastAPI()

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(product_routes)
app.include_router(category_routes)
app.include_router(internal_router)
