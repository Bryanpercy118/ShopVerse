from fastapi import APIRouter
from fastapi import Query
from app.controllers import order_controller
from app.schemas.order_schema import OrderCreate, OrderOut

router = APIRouter(prefix="/orders", tags=["Orders"])

router.post("/", response_model=OrderOut)(order_controller.create_order)
router.get("/me", response_model=list[OrderOut])(order_controller.user_orders)
router.get("/me/{order_id}", response_model=OrderOut)(order_controller.order_detail)
router.get("/admin", response_model=list[OrderOut])(order_controller.admin_orders)

router.patch("/{order_id}/status")(order_controller.update_order_status)
router.get("/stats/status")(order_controller.get_order_status_stats)
router.get("/stats/revenue")(order_controller.get_order_revenue_by_status)
