import os
import sys
import mysql.connector
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Añadir path de la app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Cargar variables de entorno
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Obtener variables del .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Crear base de datos si no existe
def create_database_if_not_exists():
    try:
        connection = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
        print(f"✅ Base de datos '{DB_NAME}' creada/verificada.")
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"❌ Error al crear la base de datos: {err}")
        sys.exit(1)

create_database_if_not_exists()

# Construir URL de conexión para SQLAlchemy
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Configuración de Alembic
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configuración de logs
if config.config_file_name:
    fileConfig(config.config_file_name)

# Importar metadata
from app.models.order_model import Base
target_metadata = Base.metadata

# Migraciones offline
def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# Migraciones online
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

# Ejecutar según modo
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
