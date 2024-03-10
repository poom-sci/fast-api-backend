import http
from core.schemas.schema import Ans, Item
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(tags=["health_checks", "status"])


#  health check endpoints
@router.get("/status", status_code=http.HTTPStatus.OK)
async def health_check():
    return JSONResponse(content={"status": "ok"})

# root endpoint
@router.get("/", status_code=http.HTTPStatus.OK)
async def default():
    return  JSONResponse(content={"status": "ok"})