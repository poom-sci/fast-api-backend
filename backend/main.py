from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import http
from typing import List, Optional
from core.schemas.schema import Ans, Item
import logging
from api.v1.v1 import router as v1Router
from api.status import router as statusRouter
from api.admin.admin import adminRouter
import sys

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from fastapi.responses import JSONResponse


app = FastAPI(title="api")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

logger.info("API is starting up")


# root endpoint
@app.get("/", status_code=http.HTTPStatus.OK)
async def default():
    print("hello world")
    return JSONResponse(content={"status": "hello world"})


app.include_router(statusRouter, prefix="/status")
app.include_router(v1Router, prefix="/v1")
app.include_router(adminRouter, prefix="/admin")
