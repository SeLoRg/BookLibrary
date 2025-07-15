import datetime
from uuid import UUID
from fastapi import Query
from pydantic import BaseModel, Extra
from typing import Optional


class BookFilter(BaseModel):
    title: Optional[str] = Query(None)
    author: Optional[str] = Query(None)
    genre: Optional[str] = Query(None)
    public_year: Optional[datetime.date] = Query(None)  # ISO 8601 формат
    pages: Optional[int] = Query(None)
    availability: Optional[bool] = Query(None)
    limit: int = Query(100, ge=1, le=1000)
    skip: int = Query(0, ge=0)


class BookSchema(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    public_year: Optional[datetime.date] = None
    pages: Optional[int] = None
    availability: Optional[bool] = None


class BookOut(BookSchema):
    id: UUID
