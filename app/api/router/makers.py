from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.cruds import makers as cruds
from app.api.entity.exceptions import AlreadyExistsError, NotFoundError
from app.api.schemas.makers import MakerCommon, MakerCreate, MakerUpdate
from app.db.database import get_db
from app.db.models import Maker

router = APIRouter()


@router.get(
    "/makers/",
    response_model=Sequence[MakerCommon],
    summary="Get all makers",
    description="Retrieve a list of all registered makers.",
)
async def read_makers(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Sequence[Maker]:

    return await cruds.get_makers(db)


@router.get(
    "/makers/{maker_id}",
    response_model=MakerCommon,
    responses={404: {"description": "Maker not found"}},
    summary="Get a maker by ID",
    description="Retrieve a single maker using its unique ID.",
)
async def read_maker(
    maker_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> Maker:
    try:
        return await cruds.get_maker(maker_id, db)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None


@router.post(
    "/makers/",
    status_code=201,
    response_model=MakerCommon,
    summary="Create a new maker",
    description="Add a new maker to the database. The maker name must be unique.",
    responses={400: {"description": "Maker already exist"}},
)
async def create_maker(
    maker: MakerCreate, db: Annotated[AsyncSession, Depends(get_db)]
) -> Maker:
    try:
        return await cruds.create_maker(maker, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None


@router.put(
    "/makers/{maker_id}",
    response_model=MakerCommon,
    summary="Update a maker's information",
    description="Update an existing maker's details.",
    responses={
        400: {"description": "Maker already exist"},
        404: {"description": "Maker not found"},
    },
)
async def update_maker(
    maker_id: int, maker: MakerUpdate, db: Annotated[AsyncSession, Depends(get_db)]
) -> Maker:

    try:
        return await cruds.update_maker(maker_id, maker, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None


@router.delete(
    "/makers/{maker_id}",
    status_code=204,
    summary="Delete a maker",
    description="Delete a maker from the database.",
    responses={404: {"description": "Maker not found"}},
)
async def delete_maker(
    maker_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> None:

    try:
        await cruds.delete_maker(maker_id, db)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None
