from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.common.crud.BookRepository import BookRepository
from src.backend.common.DB.db import db
from src.backend.library_catalog.services.LibraryCatalogService import (
    LibraryCatalogService,
)
from src.backend.common.api_clients.OpenLibraryClient import OpenLibraryClient
from src.backend.common.logging.logger import logger

open_library_client = OpenLibraryClient(base_url="https://openlibrary.org", logger=logger)


def get_open_library_client() -> OpenLibraryClient:
    return open_library_client


def get_book_repo(
    session: AsyncSession = Depends(db.get_session),
) -> BookRepository:
    return BookRepository(session=session)


def get_library_catalog_service(
    book_repo: BookRepository = Depends(get_book_repo),
    library_client: OpenLibraryClient = Depends(get_open_library_client)
) -> LibraryCatalogService:
    return LibraryCatalogService(book_repo=book_repo, library_client=library_client)
