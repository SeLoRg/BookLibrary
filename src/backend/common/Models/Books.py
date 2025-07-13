from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date as Date_DB
from datetime import date
from .Base import Base


class Books(Base):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    public_year: Mapped[date] = mapped_column(Date_DB, nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[int] = mapped_column(nullable=False)
    availability: Mapped[bool] = mapped_column(default=True)
