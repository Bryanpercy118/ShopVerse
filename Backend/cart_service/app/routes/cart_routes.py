from fastapi import APIRouter
from app.controllers import cart_controller
from app.schemas.cart_item_schema import CartItemOut, CartItemCreate, CartItemUpdate, EnrichedCartItem

router = APIRouter(prefix="/cart", tags=["Cart"])

router.get("/", response_model=list[EnrichedCartItem])(cart_controller.get_cart_details)
router.post("/", response_model=CartItemOut)(cart_controller.add_item)
router.put("/{item_id}", response_model=CartItemOut)(cart_controller.update_item)
router.delete("/{item_id}")(cart_controller.delete_item)
