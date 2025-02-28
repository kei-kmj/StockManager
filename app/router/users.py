from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.cruds import users as cruds
from app.db.database import get_db
from app.db.models import User
from app.entity.exceptions import AlreadyExistsError, NotFoundError
from app.schemas.users import UserCommon, UserCreate, UserUpdate

router = APIRouter()


@router.get(
    "/users/",
    response_model=list[UserCommon],
    summary="Get all users",
    description="Retrieve a list of all registered users.",
)
async def read_users(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Sequence[User]:

    return await cruds.get_users(db)


@router.get(
    "/users/{user_id}",
    response_model=UserCommon,
    responses={404: {"description": "User not found"}},
    summary="Get a user by ID",
    description="Retrieve a single user using its unique ID.",
)
async def read_user(user_id: int, db: Annotated[AsyncSession, Depends(get_db)]) -> User:

    try:
        return await cruds.get_user(user_id, db)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None


@router.post(
    "/users/",
    status_code=201,
    response_model=UserCommon,
    summary="Create a new user",
    description="Add a new user to the database. The user name must be unique.",
    responses={400: {"description": "User already exist"}},
)
async def create_user(
    user: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]
) -> User:

    try:
        return await cruds.create_user(user, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None


@router.put(
    "/users/{user_id}",
    response_model=UserCommon,
    summary="Update a user's information",
    description="Update an existing user's details.",
    responses={
        400: {"description": "User already exist"},
        404: {"description": "User not found"},
    },
)
async def update_user(
    user_id: int, user: UserUpdate, db: Annotated[AsyncSession, Depends(get_db)]
) -> User:

    try:
        return await cruds.update_user(user_id, user, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None


@router.delete(
    "/users/{user_id}",
    status_code=204,
    summary="Delete a user",
    description="Delete a user from the database.",
    responses={404: {"description": "User not found"}},
)
async def delete_user(
    user_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> None:

    try:
        await cruds.delete_user(user_id, db)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None
