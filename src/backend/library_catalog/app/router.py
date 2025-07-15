from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from typing import List

from src.backend.library_catalog.services.LibraryCatalogService import (
    LibraryCatalogService,
)
from src.backend.common.dependencies import get_library_catalog_service
from src.backend.library_catalog.schemas.schemas import (
    BookFilter,
    BookSchema,
    BookOut,
    BookAdd,
)

router = APIRouter(prefix="/api/books", tags=["Книги"])


@router.get("", response_model=List[BookOut])
async def get_books(
    filters: BookFilter = Depends(),
    service: LibraryCatalogService = Depends(get_library_catalog_service),
):
    filters_dict = filters.model_dump(exclude={"limit", "skip"}, exclude_none=True)
    return await service.get_books(
        limit=filters.limit or 100, skip=filters.skip or 0, **filters_dict
    )


@router.get("/{book_id}", response_model=BookOut)
async def get_book(
    book_id: UUID,
    service: LibraryCatalogService = Depends(get_library_catalog_service),
):
    return await service.get_book(book_id)


@router.post("", response_model=BookOut)
async def add_book(
    book: BookAdd,
    service: LibraryCatalogService = Depends(get_library_catalog_service),
):
    return await service.add_book(**book.model_dump(exclude_none=True))


@router.put("/{book_id}", response_model=BookOut)
async def update_book(
    book_id: UUID,
    data: BookSchema,
    service: LibraryCatalogService = Depends(get_library_catalog_service),
):
    return await service.update_book(book_id, **data.model_dump(exclude_none=True))


@router.delete("/{book_id}", status_code=204)
async def delete_book(
    book_id: UUID,
    service: LibraryCatalogService = Depends(get_library_catalog_service),
):
    await service.delete_book(book_id)
