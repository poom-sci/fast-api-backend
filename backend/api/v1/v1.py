from api.status import router as statusRouter
from fastapi import APIRouter

router = APIRouter(tags=["v1"])

# adminRouter.include_router(statusRouter, prefix="/status")
