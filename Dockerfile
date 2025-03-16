FROM python:3.13-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev
RUN pip install --no-cache-dir poetry==2.1.1
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main
COPY ./app/ /app/app/

FROM python:3.13-alpine as runtime
RUN apk add --no-cache libffi
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY --from=builder /app/app/ /app/app/
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
WORKDIR /app/app/
EXPOSE 8000
ENTRYPOINT ["uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
