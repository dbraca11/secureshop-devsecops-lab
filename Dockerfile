FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Actualizar herramientas de Python y dependencias vulnerables
RUN pip install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel \
    msgpack

# Instalar dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Eliminar el SBOM interno de pip que genera el falso positivo en Trivy
RUN rm -f /usr/local/lib/python3.11/site-packages/pip/_vendor/bom.cdx.json

COPY app ./app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
