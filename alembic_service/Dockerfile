FROM python:3.11-slim-bookworm

RUN pip install --upgrade pip && pip install poetry

WORKDIR /alembic_service

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install

COPY alembic_service .

WORKDIR /src
COPY src/backend/common ./backend/common

WORKDIR /alembic_service
