from typing import Annotated, Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.cruds import items as cruds
from app.api.entity.exceptions import (
    AlreadyExistsError,
    NotFoundError,
    RecordOperationError,
)
from app.api.schemas.items import (
    ItemCommon,
    ItemResponse,
    ItemCreate,
    ItemUpdate,
)
from app.api.schemas.schemas import ErrorResponse
from app.db.database import get_db
from app.db.models import Item

router = APIRouter()


@router.get(
    "/items",
    response_model=Sequence[ItemResponse],
    summary="Get all items",
    description="Retrieve a list of all registered items.",
)
async def read_items(
    db: Annotated[AsyncSession, Depends(get_db)],
) -> Sequence[Item]:

    return await cruds.get_items(db)


@router.get(
    "/items/{item_id}",
    response_model=ItemResponse,
    responses={404: {
        "model":ErrorResponse,
        "description": "Item not found"}},
    summary="Get a item by ID",
    description="Retrieve a single item using its unique ID.",
)
async def read_item(
    item_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> Item:

    try:
        return await cruds.get_item(item_id, db)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None


@router.post(
    "/items",
    status_code=201,
    response_model=ItemCommon,
    summary="Create a new item",
    description="Add a new item to the database. The tem name must be unique.",
    responses={
        400: {"description": "Maker already exist"},
        500: {"description": "Record create error"},
    },
)
async def create_item(
    item: ItemCreate, db: Annotated[AsyncSession, Depends(get_db)]
) -> Item:

    try:
        return await cruds.create_item(item, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None

    except RecordOperationError as e:
        raise HTTPException(status_code=500, detail=str(e)) from None


@router.put(
    "/items/{item_id}",
    response_model=ItemCommon,
    summary="Update a item's information",
    description="Update an existing item's details.",
    responses={
        400: {"description": "Item already exist"},
        404: {"description": "Item not found"},
        500: {"description": "Record update error"},
    },
)
async def update_item(
    item_id: int, item: ItemUpdate, db: Annotated[AsyncSession, Depends(get_db)]
) -> Item:

    try:
        return await cruds.update_item(item_id, item, db)

    except AlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e)) from None

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None

    except RecordOperationError as e:
        raise HTTPException(status_code=500, detail=str(e)) from None


@router.delete(
    "/items/{item_id}",
    status_code=204,
    summary="Delete a item",
    description="Delete a item from the database.",
    responses={
        404: {"description": "Maker not found"},
        500: {"description": "Record delete error"},
    },
)
async def delete_item(
    item_id: int, db: Annotated[AsyncSession, Depends(get_db)]
) -> None:

    try:
        await cruds.delete_item(item_id, db)

    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from None

    except RecordOperationError as e:
        raise HTTPException(status_code=500, detail=str(e)) from None
