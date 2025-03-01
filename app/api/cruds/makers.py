import re
import unicodedata
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Maker
from app.api.entity.exceptions import AlreadyExistsError, NotFoundError
from app.api.schemas.makers import MakerCreate, MakerUpdate


def normalize_company_name(name: str) -> str:
    """メーカー名を正規化（"株式会社" や "（株）" を削除し、全角・半角を統一）"""

    trimmed_name = re.sub(r"\(株\)|株式会社", "", name).strip()
    normalized_name = unicodedata.normalize("NFKC", trimmed_name)

    return normalized_name


async def get_makers(db: AsyncSession) -> Sequence[Maker]:
    found_maker = await db.execute(select(Maker))
    return found_maker.scalars().all()


async def get_maker(maker_id: int, db: AsyncSession) -> Maker:
    query = await db.execute(select(Maker).filter(Maker.id == maker_id))
    found_maker = query.scalars().first()

    if not found_maker:
        raise NotFoundError(f"Maker ID {maker_id} not found")

    return found_maker


async def create_maker(maker: MakerCreate, db: AsyncSession) -> Maker:

    normalized_name = normalize_company_name(maker.name)

    existing_maker = await db.execute(
        select(Maker).filter(Maker.name == normalized_name)
    )

    if existing_maker.scalars().first():
        raise AlreadyExistsError("Maker name already exists (normalized check)")

    new_maker = Maker(**maker.model_dump())

    db.add(new_maker)
    await db.commit()
    await db.refresh(new_maker)

    return new_maker


async def update_maker(maker_id: int, maker: MakerUpdate, db: AsyncSession) -> Maker:

    query = await db.execute(select(Maker).filter(Maker.id == maker_id))
    found_maker = query.scalars().first()

    if not found_maker:
        raise NotFoundError(f"Maker ID {maker_id} not found")

    normalized_name = normalize_company_name(maker.name)

    existing_maker = await db.execute(
        select(Maker).filter(Maker.name == normalized_name)
    )
    if existing_maker.scalars().first():
        raise AlreadyExistsError("Maker name already exists (normalized check)")

    found_maker.name = normalized_name

    await db.commit()
    await db.refresh(found_maker)

    return found_maker


async def delete_maker(maker_id: int, db: AsyncSession) -> None:
    query = await db.execute(select(Maker).filter(Maker.id == maker_id))
    found_maker = query.scalars().first()

    if not found_maker:
        raise NotFoundError(f"Maker ID {maker_id} not found")

    await db.delete(found_maker)
    await db.commit()
