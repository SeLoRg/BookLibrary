import datetime
from pydantic import BaseModel, Extra
from typing import Optional


class BookSchema(BaseModel):
    title: Optional[str]
    author: Optional[str]
    genre: Optional[str]
    public_year: Optional[datetime.date]
    pages: Optional[int]
    availability: Optional[bool]


class BookFilter(BookSchema):
    limit: Optional[int] = 100
    skip: Optional[int] = 0
