
from fastapi import APIRouter
import http
from core.service.transformer import predict

router = APIRouter(tags=["v1"])

# adminRouter.include_router(statusRouter, prefix="/status")

# test endpoint
@router.post("/test/{text}", status_code=http.HTTPStatus.OK)
async def test( text: str):
    res = predict(text)
    return {"status": "ok", "message": "test", "req":text,"res": res}