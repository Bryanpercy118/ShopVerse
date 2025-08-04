from fastapi import APIRouter, Depends
from app.shared.jwt_bearer import JWTBearer
from app.controllers import category_controller

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    dependencies=[Depends(JWTBearer())]
)

router.post("/", response_model=category_controller.Category)(category_controller.create_category)
router.get("/", response_model=list[category_controller.Category])(category_controller.get_categories)
router.get("/{category_id}", response_model=category_controller.Category)(category_controller.get_category)
router.put("/{category_id}", response_model=category_controller.Category)(category_controller.update_category)
router.delete("/{category_id}")(category_controller.delete_category)
