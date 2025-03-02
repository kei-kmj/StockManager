from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.cruds import closings as cruds
from app.api.entity.exceptions import (
    AlreadyExistsError,
    RecordOperationError,
)
from app.api.schemas.closings import ClosingCommon, ClosingCreate
from app.db.database import get_db
from app.db.models import Closing

router = APIRouter()


@router.get(
    "/closings/latest", response_model=ClosingCommon, summary="Get a latest closing"
)
async def read_closing(db: Annotated[AsyncSession, Depends(get_db)]) -> Closing | None:

    return await cruds.get_latest_closing(db)


@router.post(
    "/closings/",
    status_code=201,
    response_model=ClosingCommon,
    summary="Create a new closing",
    description="Add a new closing to the database.",
    responses={
        400: {"description": "Closing already exist"},
        500: {"description": "Record create error"},
    },
)
async def create_closing(
    closing: ClosingCreate, db: Annotated[AsyncSession, Depends(get_db)]
) -> None:

    try:
        return await cruds.create_closing(closing, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None

    except RecordOperationError as e:
        raise HTTPException(status_code=500, detail=str(e)) from None
