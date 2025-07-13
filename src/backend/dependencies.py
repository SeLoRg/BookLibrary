from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.common.crud.BookRepository import BookRepository
from src.backend.common.DB.db import db
from src.backend.library_catalog.services.LibraryCatalogService import (
    LibraryCatalogService,
)


def get_book_repo(
    session: AsyncSession = Depends(db.get_session),
) -> BookRepository:
    return BookRepository(session=session)


def get_library_catalog_service(
    book_repo: BookRepository = Depends(get_book_repo),
) -> LibraryCatalogService:
    return LibraryCatalogService(book_repo=book_repo)
