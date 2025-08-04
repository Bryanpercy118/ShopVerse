from fastapi import APIRouter, Depends
from app.shared.jwt_bearer import JWTBearer
from app.controllers import product_controller
from app.schemas.product_schema import Product as ProductOut

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    dependencies=[Depends(JWTBearer())]
)

router.post("/", response_model=ProductOut)(product_controller.create_product)
router.get("/", response_model=list[ProductOut])(product_controller.get_products)
router.get("/{product_id}", response_model=ProductOut)(product_controller.get_product)
router.put("/{product_id}", response_model=ProductOut)(product_controller.update_product)
router.delete("/{product_id}")(product_controller.delete_product)

