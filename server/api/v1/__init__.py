from fastapi import APIRouter

from .reviews import router as reviews_router

router = APIRouter()  # Must be prefix="/v1"
router.include_router(router=reviews_router)
