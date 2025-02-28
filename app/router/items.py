from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.cruds import users as cruds
from app.db.database import get_db
from app.db.models import User
from app.schemas.users import UserCommon, UserCreate

router = APIRouter()


@router.get("/users/", response_model=list[UserCommon])
async def read_users(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Sequence[User]:

    return await cruds.get_users(db)


@router.get("/users/{user_id}", response_model=UserCommon)
async def read_user(
    user_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> User | None:

    return await cruds.get_user(user_id, db)


@router.post("/users/", status_code=201, response_model=UserCommon)
async def create_user(
    user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]
) -> User:

    return await cruds.create_user(user, db)


@router.put("/users/{user_id}", response_model=UserCommon)
async def update_user(
    user_id: int, user: UserCommon, db: Annotated[AsyncSession, Depends(get_db)]
) -> User | None:

    result = await cruds.update_user(user_id, user, db)

    if not result:
        raise HTTPException(status_code=404, detail="user not found")

    return result


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> None:

    await cruds.delete_user(user_id, db)
