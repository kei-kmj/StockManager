from typing import Sequence, Optional, Annotated

from fastapi import APIRouter, Query, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.entity.exceptions import AlreadyExistsError, RecordOperationError
from app.api.schemas.stock_events import StockEventResponse, StockEventCreate, StockEventCommon
from app.db.database import get_db
from app.db.models import StockEvent

from app.api.cruds import stock_events as cruds

router = APIRouter()

@router.get(
    "stock_events",
    response_model=Sequence[StockEventResponse],
    summary="Get stock event",
)
async def read_events(
        db: Annotated[AsyncSession, Depends(get_db)],
        item_id: Optional[int] = Query(None, description="アイテムIDでフィルタ"),
        actor_id: Optional[int] = Query(None, description="実行者のユーザーIDでフィルタ"),
        event_type: Optional[int] = Query(None, description="イベントタイプでフィルタ"),
        limit: Optional[int] = Query(None, description="取得する最大件数"),
        offset: Optional[int] = Query(None, description="オフセット"),
) -> Sequence[StockEventResponse]:

    return await cruds.get_stock_events(db, item_id, actor_id, event_type, limit, offset)


@router.post(
    "stock_events",
    status_code=201,
    response_model=StockEventCommon,
    responses={500: {"description": "Record update error"}}
)
async def create_stock_events(
        event: StockEventCreate,
        db: Annotated[AsyncSession, Depends(get_db)],
) -> StockEvent:
    try:
        return await cruds.create_stock_events(event, db)

    except RecordOperationError as e:
        raise HTTPException(status_code=500, detail=str(e)) from None
