

# ShopVerse - Sistema de Comercio Electrónico - PRUEBA TECNICA 

**ShopVerse** es una plataforma de comercio electrónico moderna construida con una arquitectura de microservicios desacoplados, que permite gestionar productos, carritos, pedidos y autenticación de usuarios (admin y cliente), todo respaldado por un frontend agradable y responsivo con Angular.

## Arquitectura General

```

SHOPVERSE/
├── Backend/
│   ├── auth/               # Servicio de autenticación (registro/login, JWT)
│   ├── cart\_service/       # Servicio de carrito de compras
│   ├── order\_service/      # Servicio de pedidos y estadísticas
│   ├── product\_service/    # Gestión de productos y categorías
├── Frontend/
│   └── shopverse-frontend/ # Aplicación Angular standalone
├── docker-compose.yml      # Orquestador de contenedores

````

## Tecnologías Usadas

| Capa        | Tecnologías                                   |
|-------------|-----------------------------------------------|
| Frontend    | Angular 17 (standalone), TailwindCSS          |
| Backend     | FastAPI, SQLAlchemy, JWT                      |
| Base de Datos | MySQL / PostgreSQL (según configuración)   |
| Contenedores| Docker, Docker Compose                        |
| Seguridad   | Autenticación JWT, Roles (`admin`, `customer`)|

---

## Microservicios

| Servicio         | Puerto | Descripción                             |
|------------------|--------|-----------------------------------------|
| `auth/`          | 8001   | Registro, login, autenticación          |
| `product_service/` | 8002 | CRUD de productos y categorías          |
| `cart_service/`  | 8003   | Operaciones del carrito                 |
| `order_service/` | 8004   | Gestión de pedidos y estadísticas       |
| `frontend/`      | 4200   | Interfaz Angular responsiva             |

---

## Base de Datos & Migraciones

Las migraciones y creación automática de base de datos se gestionan con **Alembic** utilizando el ORM de SQLAlchemy.

- Si la base de datos no existe, será creada automáticamente al correr Alembic.
- Las migraciones se aplican a través del archivo `env.py` que extiende la lógica estándar para leer variables `.env` y preparar el entorno.

### Comando para aplicar migraciones:

```bash
alembic upgrade head
````

> Nota: Este comportamiento está incluido para cada microservicio que use base de datos, iniciando su motor y esquema automáticamente si es necesario.

---

## Funcionalidades Clave

* Login y Registro con roles (`admin`, `customer`)
* Dashboard administrativo con métricas:

  * Pedidos completados
  * Ingresos por estado
  * Productos en stock
  * Usuarios registrados
* Carrito de compras interactivo
* Gestión visual de pedidos con seguimiento de estado (`pendiente`, `enviado`)
* Acceso exclusivo del cliente a sus propios pedidos

---

## Pruebas Unitarias

Pruebas implementadas para servicios principales (`auth`, `orders`).

```bash
pytest
```

---

## Caso de Uso - Compra Cliente

**Actor:** Cliente registrado
**Escenario:**

1. El usuario inicia sesión
2. Explora productos y los agrega al carrito
3. Realiza el pedido
4. Visualiza sus pedidos y su estado actualizado por el administrador

---

## Cómo Iniciar el Proyecto

### Requisitos

* Python 3.10+
* Node.js
* Docker (recomendado)

### Inicio con Docker

```bash
docker-compose up --build
```

### Manualmente

#### Backend

```bash
cd Backend/auth && uvicorn main:app --reload --port 8001
cd Backend/product_service && uvicorn main:app --reload --port 8002
cd Backend/cart_service && uvicorn main:app --reload --port 8003
cd Backend/order_service && uvicorn main:app --reload --port 8004
```

#### Frontend

```bash
cd Frontend/shopverse-frontend
npm install
ng serve
```

---

## Contacto

> Bryan Andrés Granados Percy
> 📱 322 587 4350
> 📧 [bryanpercy77@gmail.com](mailto:bryanpercy77@gmail.com)

Repositorio: (Privado, será entregado al área de Gerencia de Proyectos de Develop App)

---

## Seguridad y Roles

| Rol      | Permisos                                                                 |
| -------- | ------------------------------------------------------------------------ |
| Admin    | Acceso completo: dashboard, métricas, todos los pedidos y CRUD productos |
| Customer | Ver productos, realizar pedidos, ver solo sus pedidos                    |

---

© 2025 - ShopVerse Project - Desarrollado por Bryan A. Granados Percy
