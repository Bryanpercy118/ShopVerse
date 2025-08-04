FROM python:3.11-slim

WORKDIR /app

# Copiar archivos del microservicio
COPY ./app /app/app
COPY alembic.ini .
COPY requirements.txt .
COPY entrypoint.sh .
COPY alembic /app/alembic

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Permisos de ejecución
RUN chmod +x entrypoint.sh

CMD ["bash", "entrypoint.sh"]
