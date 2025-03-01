from sqlite3 import IntegrityError
from typing import Sequence

from sqlalchemy import select, Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.db.models import Item, Maker
from app.entity.exceptions import NotFoundError, AlreadyExistsError
from app.schemas.items import ItemCreate, ItemUpdate


async def is_duplicate_item(name: str, maker_id: int, db:AsyncSession) -> bool:
    query = await db.execute(select(Item).filter(Item.name == name, Item.maker_id == maker_id))

    return query.scalars().first() is not None


async def get_items(db: AsyncSession) -> Sequence[Item]:
    result = await db.execute(select(Item).options(joinedload(Item.maker)))
    return result.scalars().all()


async def get_item(item_id: int, db: AsyncSession) -> Item | None:
    query = await db.execute(
        select(Item).options(joinedload(Item.maker)).filter(Item.id == item_id)
    )
    found_item = query.scalars().first()

    if not found_item:
        raise NotFoundError(f"Maker ID {item_id} not found")

    return found_item


async def create_item(item: ItemCreate, db: AsyncSession) -> Item:

    query = await db.execute(select(Maker).where(Maker.id == item.maker_id))
    found_item = query.scalars().first()

    if not found_item:
        raise AlreadyExistsError("Item name already exists (normalized check)")

    new_item = Item(**item.model_dump())

    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item


async def update_item(item_id: int, item: ItemUpdate, db: AsyncSession) -> Item:

    query = await db.execute(Select(Item).filter(Item.id == item_id))
    found_item: Item | None = query.scalars().first()

    if not found_item:
        raise NotFoundError(f"Item ID {item_id} not found")

    if is_duplicate_item(item.name, item.maker_id, db):
        raise AlreadyExistsError( "item name already exists" )

    found_item.name = item.name
    found_item.maker_id = item.maker_id

    await db.commit()
    await db.refresh(found_item)

    return found_item




async def delete_item(item_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(Item).filter(Item.id == item_id))
    found_item = result.scalars().first()

    if not found_item:
        raise NotFoundError(f"Maker ID {item_id} not found")

    await db.delete(found_item)
    await db.commit()
