from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User
from app.entity.exceptions import AlreadyExistsError, NotFoundError
from app.schemas.users import UserCreate, UserUpdate


async def is_duplicate_email(email: str, db: AsyncSession) -> bool:
    """emailが一致するかチェック"""
    query = await db.execute(select(User).where(User.email == email))
    return query.scalars().first() is not None


async def is_duplicate_nickname(nickname: str, db: AsyncSession) -> bool:
    """`nickname` が既に存在するかチェック"""
    query = await db.execute(select(User).where(User.nickname == nickname))
    return query.scalars().first() is not None


async def get_users(db: AsyncSession) -> Sequence[User]:
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user(user_id: int, db: AsyncSession) -> User:
    query = await db.execute(select(User).filter(User.id == user_id))
    found_user = query.scalars().first()

    if not found_user:
        raise NotFoundError(f"Maker ID {user_id} not found")

    return found_user


async def create_user(user: UserCreate, db: AsyncSession) -> User:

    if await is_duplicate_email(user.email, db):
        raise AlreadyExistsError(f"User this email {user.email} already exists")

    if await is_duplicate_nickname(user.nickname, db):
        raise AlreadyExistsError(
            f"User with this nickname {user.nickname} already exists"
        )

    new_user = User(**user.model_dump())

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


async def update_user(user_id: int, user: UserUpdate, db: AsyncSession) -> User:
    query = await db.execute(select(User).filter(User.id == user_id))
    found_user = query.scalars().first()

    if not found_user:
        raise NotFoundError(f"User ID {user_id} not found")

    found_user.name = user.name
    found_user.email = user.email

    await db.commit()
    await db.refresh(found_user)

    return found_user


async def delete_user(user_id: int, db: AsyncSession) -> None:
    query = await db.execute(select(User).filter(User.id == user_id))
    found_user = query.scalars().first()

    if not found_user:
        raise NotFoundError(f"User ID {user_id} not found")

    await db.delete(found_user)
    await db.commit()
