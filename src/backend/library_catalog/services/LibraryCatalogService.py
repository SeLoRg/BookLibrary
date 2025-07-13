from uuid import UUID
from src.backend.common.crud.BookRepository import BookRepository
from src.backend.common.Models import Books
from src.backend.common.exceptions.exceptions import ServiceError
from src.backend.common.logging.logger import logger
from typing import Optional, List


class LibraryCatalogService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    async def get_books(
        self, limit: int = 100, skip: int = 0, **filters
    ) -> List[Books]:
        try:
            return await self.book_repo.get_by_filter(limit=limit, skip=skip, **filters)
        except Exception as e:
            logger.error(f"Ошибка при получении списка книг: {e}", exc_info=True)
            raise ServiceError("Не удалось получить список книг")

    async def get_book(self, book_id: UUID) -> Optional[Books]:
        try:
            books = await self.book_repo.get_by_filter(id=book_id)
            if not books:
                raise ServiceError(f"Книга с id={book_id} не найдена", status_code=404)
            return books[0]
        except ServiceError:
            raise
        except Exception as e:
            logger.error(f"Ошибка при получении книги: {e}", exc_info=True)
            raise ServiceError("Не удалось получить книгу")

    async def add_book(self, **book_data) -> Books:
        try:
            new_book: Books = await self.book_repo.create(**book_data)
            await self.book_repo.session.commit()
            return new_book
        except Exception as e:
            logger.error(f"Ошибка при добавлении книги: {e}", exc_info=True)
            raise ServiceError("Не удалось добавить книгу")

    async def update_book(self, book_id: UUID, **update_data) -> Optional[Books]:
        try:
            book = await self.book_repo.update_by_id(object_id=book_id, **update_data)
            if not book:
                raise ServiceError(f"Книга с id={book_id} не найдена", status_code=404)
            await self.book_repo.session.commit()

            return book
        except ServiceError:
            raise
        except Exception as e:
            logger.error(f"Ошибка при обновлении книги: {e}", exc_info=True)
            raise ServiceError("Не удалось обновить книгу")

    async def delete_book(self, book_id: UUID) -> None:
        try:
            await self.book_repo.delete_by_id(object_id=book_id)
            await self.book_repo.session.commit()
        except Exception as e:
            logger.error(f"Ошибка при удалении книги: {e}", exc_info=True)
            raise ServiceError("Не удалось удалить книгу")
