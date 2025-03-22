from datetime import datetime
from typing import Optional

from app.api.schemas.items import ItemResponse
from app.api.schemas.schemas import BaseSchema
from app.api.schemas.users import UserCommon


class StockEventCreate(BaseSchema):
    actor_id: int
    item_id: int
    event_type: int
    quantity: int
    note: Optional[int]


class StockEventCommon(StockEventCreate):
    id: int
    event_date: datetime


class StockEventResponse(StockEventCommon):
    user: UserCommon
    item: ItemResponse
