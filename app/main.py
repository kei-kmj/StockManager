from contextlib import asynccontextmanager, closing
from typing import AsyncGenerator

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.router.closings import router as closing_router
from app.api.router.items import router as item_router
from app.api.router.makers import router as maker_router
from app.api.router.users import router as user_router
from app.api.router.stock_events import router as stock_events_router

from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:  # noqa: ARG001
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @appはFastAPIのインスタンス
app.include_router(user_router, tags=["Users"])
app.include_router(maker_router, tags=["Makers"])
app.include_router(item_router, tags=["Items"])
app.include_router(closing_router, tags=["Closings"])
app.include_router(stock_events_router, tags=["Stock Events"])
