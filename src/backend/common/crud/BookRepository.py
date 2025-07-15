from sqlalchemy.ext.asyncio import AsyncSession

from .CrudDB import CrudDB
from src.backend.common.Models import Books


class BookRepository(CrudDB[Books]):

    def __init__(self, session: AsyncSession):
        super().__init__(model=Books, session=session)
