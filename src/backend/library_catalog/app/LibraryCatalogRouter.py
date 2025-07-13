from fastapi import APIRouter, Depends, HTTPException
from src.backend.library_catalog.services.LibraryCatalogService import (
    LibraryCatalogService,
)
from src.backend.common.dependencies import get_library_catalog_service
from src.backend.common.Models import Books
from typing import List
from src.backend.common.logging.log_funces import log_route
from src.backend.library_catalog.schemas.schemas import *


class LibraryCatalogRouter:
    def __init__(self):
        self.router = APIRouter(prefix="/books", tags=["Книги"])
        self.router.add_api_route("", log_route(self.get_books), methods=["GET"])
        self.router.add_api_route(
            "/{book_id}", log_route(self.get_book), methods=["GET"]
        )
        self.router.add_api_route("", log_route(self.add_book), methods=["POST"])
        self.router.add_api_route(
            "/{book_id}", log_route(self.update_book), methods=["PUT"]
        )
        self.router.add_api_route(
            "/{book_id}", log_route(self.delete_book), methods=["DELETE"]
        )

    async def get_books(
        self,
        filters: BookFilter = Depends(),
        service: LibraryCatalogService = Depends(get_library_catalog_service),
    ) -> List[Books]:
        filters_dict: dict = filters.model_dump(
            exclude={"limit", "skip"}, exclude_none=True
        )
        return await service.get_books(**filters_dict)

    async def get_book(
        self,
        book_id: int,
        service: LibraryCatalogService = Depends(get_library_catalog_service),
    ) -> Books:
        book = await service.get_book(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return book

    async def add_book(
        self,
        book: BookSchema,
        service: LibraryCatalogService = Depends(get_library_catalog_service),
    ) -> Books:
        return await service.add_book(**book.model_dump(exclude_none=True))

    async def update_book(
        self,
        book_id: int,
        data: BookSchema,
        service: LibraryCatalogService = Depends(get_library_catalog_service),
    ) -> Books:
        return await service.update_book(book_id, **data.model_dump(exclude_none=True))

    async def delete_book(
        self,
        book_id: int,
        service: LibraryCatalogService = Depends(get_library_catalog_service),
    ) -> None:
        await service.delete_book(book_id)
