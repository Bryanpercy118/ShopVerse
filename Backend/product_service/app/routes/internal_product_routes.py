from fastapi import APIRouter
from app.controllers import product_controller
from app.schemas.product_schema import Product as ProductOut

router = APIRouter(
    prefix="/internal/products",
    tags=["Internal Products"]
)

router.get("/{product_id}", response_model=ProductOut)(product_controller.internal_get_product)
