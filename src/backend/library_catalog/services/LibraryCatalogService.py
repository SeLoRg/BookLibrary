from src.backend.common.crud.BookRepository import BookRepository
from src.backend.common.Models import Books
from typing import Optional, List


class LibraryCatalogService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    async def get_books(
        self, limit: int = 100, skip: int = 0, **filters
    ) -> List[Books]:
        """Получение списка всех книг с возможностью фильтрации"""
        return await self.book_repo.get_by_filter(limit=limit, skip=skip, **filters)

    async def get_book(self, book_id: int) -> Optional[Books]:
        """Получение информации о конкретной книге по id"""
        books = await self.book_repo.get_by_filter(id=book_id)
        return books[0] if books else None

    async def add_book(self, **book_data) -> Books:
        """Добавление новой книги в каталог"""
        return await self.book_repo.create(**book_data)

    async def update_book(self, book_id: int, **update_data) -> Optional[Books]:
        """Обновление информации о книге"""
        return await self.book_repo.update_by_id(object_id=book_id, **update_data)

    async def delete_book(self, book_id: int) -> None:
        """Удаление книги из каталога"""
        await self.book_repo.delete_by_id(object_id=book_id)
