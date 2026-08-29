FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends openssl=3.0.15-1~deb12u1 libssl3t64=3.0.15-1~deb12u1 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip==24.2 && \
    pip uninstall -y setuptools

RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt

COPY app ./app

RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
