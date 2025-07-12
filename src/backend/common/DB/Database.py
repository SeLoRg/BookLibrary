from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from src.backend.common.Core.config import settings


class Database:
    __instance = None
    __slots__ = ("_async_engine", "_async_session_factory", "_initialized")

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance

    def __init__(self, url: str, echo=True):
        if getattr(self, "_initialized", False):
            return

        self._async_engine = create_async_engine(url=url, echo=echo)
        self._async_session_factory = async_sessionmaker(
            bind=self._async_engine, autoflush=False, autocommit=False
        )
        self._initialized = True

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        async with self._async_session_factory() as session:
            yield session

    @property
    def async_session_factory(self):
        return self._async_session_factory


database = Database(url=settings.postgres_url, echo=False)
