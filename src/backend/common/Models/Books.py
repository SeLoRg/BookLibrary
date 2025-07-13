from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime as Datetime_DB
from datetime import datetime
from .Base import Base


class Books(Base):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    public_year: Mapped[datetime] = mapped_column(Datetime_DB, nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[int] = mapped_column(nullable=False)
    availability: Mapped[bool] = mapped_column(default=True)
