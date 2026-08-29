FROM python:3.12-slim

WORKDIR /app

# Actualizar paquetes del sistema operativo para resolver CVEs de Debian
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt-get/lists/*

# Actualizar pip, setuptools y wheel a versiones seguras
RUN pip install --no-cache-dir --upgrade pip setuptools>=79.0.0 wheel>=0.46.3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
