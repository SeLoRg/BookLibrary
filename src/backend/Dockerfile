FROM python:3.11-slim

RUN pip install --upgrade pip && pip install poetry

WORKDIR /src

COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && poetry install

COPY ./src .
WORKDIR /
CMD ["uvicorn", "src.backend.main:app", "--host", "0.0.0.0", "--port", "8002", "--reload", "--reload-dir", "src"]