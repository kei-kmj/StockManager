from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import User
from app.schemas.users import UserCommon, UserCreate


async def get_users(db: AsyncSession) -> Sequence[User]:
    result = await db.execute(select(User))
    return result.scalars().all()


async def get_user(user_id: int, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).filter(User.id == user_id))

    return result.scalars().first()


async def create_user(user: UserCreate, db: AsyncSession) -> User:
    db_user = User(**user.model_dump())

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user


async def update_user(user_id: int, user: UserCommon, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()

    if not db_user:
        return None

    db_user.name = user.name
    db_user.email = user.email

    await db.commit()
    await db.refresh(db_user)

    return db_user


async def delete_user(user_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()

    if not db_user:
        return None

    await db.delete(db_user)
    await db.commit()
