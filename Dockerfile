FROM python:3.11-slim

WORKDIR /app

# Actualiza el SO (mantiene 0 vulnerabilidades en Debian)
RUN apt-get update && apt-get install -y --no-install-recommends openssl libssl3t64 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Forzamos la actualización de pip, setuptools (>=78.1.1) y msgpack (>=1.2.1)
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel -r requirements.txt

COPY app ./app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
