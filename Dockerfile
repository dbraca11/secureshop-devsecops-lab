cat <<'EOF' > Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Actualizar el SO para corregir vulnerabilidades de OpenSSL / Debian
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt-get/lists/*

# Actualizar herramientas de construcción de Python
RUN pip install --no-cache-dir --upgrade pip setuptools>=79.0.0 wheel>=0.46.3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF
