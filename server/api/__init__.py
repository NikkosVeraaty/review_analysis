from fastapi import APIRouter

from .v1 import router as v1_router

router = APIRouter()  # Must be prefix="/api"
router.include_router(router=v1_router)
