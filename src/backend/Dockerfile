FROM python:3.11-slim

WORKDIR /src
COPY req.txt ./backend/req.txt

RUN pip install --upgrade pip && pip install -r ./backend/req.txt

COPY . ./backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]