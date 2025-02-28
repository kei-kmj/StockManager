from datetime import datetime

from app.schemas.schemas import BaseSchema


class UserCreate(BaseSchema):
    name: str
    email: str


class UserCommon(UserCreate):
    id: int
    created_at: datetime
