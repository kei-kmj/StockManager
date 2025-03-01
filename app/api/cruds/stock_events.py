from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.entity.exceptions import RecordOperationError
from app.api.schemas.stock_events import StockEventCreate
from app.db.models import StockEvent


async def get_stock_events(
    db: AsyncSession,
    item_id: Optional[int],
    actor_id: Optional[int],
    event_type: Optional[int],
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> Sequence[StockEvent]:
    query = select(StockEvent)

    if item_id:
        query = query.filter(StockEvent.item_id == item_id)

    if actor_id:
        query = query.filter(StockEvent.actor_id == actor_id)

    if event_type:
        query = query.filter(StockEvent.event_type == event_type)

    query = query.limit(limit).offset(offset)
    filtered_event = (await db.execute(query)).scalars().all()

    return filtered_event


async def create_stock_events(event: StockEventCreate, db: AsyncSession) -> StockEvent:

    new_event = StockEvent(**event.model_dump())

    try:
        await db.commit()
        await db.refresh(new_event)
        return new_event

    except Exception as e:
        await db.rollback()
        raise RecordOperationError(f"登録に失敗しました: {str(e)}") from None
