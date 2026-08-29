FROM python:3.11-slim

WORKDIR /app

# Actualiza paquetes del sistema operativo para arreglar OpenSSL/libssl3t64
RUN apt-get update && apt-get install -y --no-install-recommends openssl libssl3t64 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# Actualiza setuptools/wheel para corregir jaraco.context y wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel -r requirements.txt

COPY app ./app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
