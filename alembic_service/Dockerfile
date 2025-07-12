FROM python:3.11-slim-bookworm

RUN pip install --upgrade pip
WORKDIR /alembic_service
COPY alembic_service/req.txt ./req.txt
RUN pip install -r ./req.txt

COPY alembic_service .

WORKDIR /src
COPY src/backend/common ./backend/common

WORKDIR /alembic_service
