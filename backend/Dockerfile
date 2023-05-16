# backend/Dockerfile

FROM python:3.9.16-slim AS builder

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# python dependencies 관리
RUN pip install poetry==1.4.0 \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-ansi --no-root \
    && poetry export -f requirements.txt >> requirements.txt

# ---

FROM python:3.9.16-slim
WORKDIR /app

COPY --from=builder /app/requirements.txt /app
COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt
EXPOSE 8080

CMD ["python3", "main.py"]