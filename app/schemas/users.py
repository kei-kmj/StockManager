from datetime import datetime

from app.schemas.schemas import BaseSchema


class UserCreate(BaseSchema):
    name: str
    nickname: str
    email: str


class UserUpdate(UserCreate):
    pass


class UserCommon(UserCreate):
    id: int
    created_at: datetime
