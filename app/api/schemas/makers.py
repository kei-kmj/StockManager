from datetime import datetime

from app.api.schemas.schemas import BaseSchema


class MakerCreate(BaseSchema):
    name: str


class MakerUpdate(MakerCreate):
    pass


class MakerCommon(MakerCreate):
    id: int
    created_at: datetime
