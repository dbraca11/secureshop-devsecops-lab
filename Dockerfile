FROM python:3.11-slim

WORKDIR /app

# 1. Actualiza paquetes del sistema operativo Debian
RUN apt-get update && apt-get install -y --no-install-recommends openssl libssl3t64 && rm -rf /var/lib/apt/lists/*

# 2. Fuerza la actualización explícita e ignora la caché para fijar las versiones seguras
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .

# 3. Instala tus dependencias respetando los paquetes ya actualizados arriba
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
