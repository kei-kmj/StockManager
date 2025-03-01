from datetime import datetime

from app.schemas.makers import MakerCommon
from app.schemas.schemas import BaseSchema


class ItemCreate(BaseSchema):
    name: str
    maker_id: int


class ItemUpdate(ItemCreate):
    pass


class ItemCommon(ItemCreate):
    id: int
    created_at: datetime


class ItemResponse(ItemCommon):
    maker: MakerCommon
