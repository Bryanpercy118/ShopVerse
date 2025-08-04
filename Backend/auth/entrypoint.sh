echo "Migrando base de datos..."
alembic upgrade head

echo "Ejecutando seeder..."
PYTHONPATH=app python app/seeders/init_seed.py

echo "Iniciando servicio..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
