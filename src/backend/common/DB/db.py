from .Database import Database
from src.backend.common.Core.config import settings

db = Database(url=settings.postgres_url, echo=False)
