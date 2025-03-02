from datetime import timedelta, date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.cruds.inventory_snapshots import create_inventory_snapshots
from app.api.entity.exceptions import InvalidDataError, RecordOperationError
from app.api.schemas.closings import ClosingCreate
from app.db.models import Closing


async def get_latest_closing(db: AsyncSession):
    query = await db.execute(
        select(Closing)
        .filter(Closing.is_closed == True)
        .order_by(Closing.closing_date.desc())
    )
    latest_closing = query.scalars().first()

    if not latest_closing:
        today = date.today()
        first_of_this_month = today.replace(day=1)
        latest_closing_date = first_of_this_month - timedelta(days=1)

        return Closing(closing_date=latest_closing_date, is_closed=False)

    return latest_closing


async def create_closing(closing : ClosingCreate, db: AsyncSession):

    try:
        latest_closing = await get_latest_closing(db)
        allowed_closing_date = (latest_closing.closing_date.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1)

        if closing.closing_date != allowed_closing_date:
            raise InvalidDataError(f"Invalid closing date: {closing.closing_date}. Expected next closing date is {allowed_closing_date}.")


        new_closing = (Closing(**closing.model_dump()))
        db.add(new_closing)

        year, month = closing.closing_date.year, closing.closing_date.month
        await create_inventory_snapshots(year, month, db)

    except Exception as e:
        await db.rollback()

        raise RecordOperationError(f"Failed to close inventory: {str(e)}")





