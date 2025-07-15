from uuid import UUID
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import UUID as PG_UUID
import uuid


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
