from datetime import datetime

from app.api.schemas.makers import MakerCommon
from app.api.schemas.schemas import BaseSchema


class ItemCreate(BaseSchema):
    name: str
    maker_id: int


class ItemUpdate(ItemCreate):
    pass


class ClosiongCommon(ItemCreate):
    id: int
    created_at: datetime


class ClosiongResponse(ClosiongCommon):
    maker: MakerCommon
