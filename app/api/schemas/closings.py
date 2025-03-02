from datetime import date, datetime, timedelta

from pydantic import Field

from app.api.schemas.schemas import BaseSchema


class ClosingCreate(BaseSchema):
    closing_date: date = Field(
        default_factory=lambda: (date.today().replace(day=1) - timedelta(days=1))
    )
    is_closed: bool


class ClosingUpdate(ClosingCreate):
    pass


class ClosingCommon(ClosingCreate):
    id: int
    created_at: datetime
