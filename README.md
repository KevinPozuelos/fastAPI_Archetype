# fastAPI_Archetype
Proyecto base para el desarrollo de API en FastApi Utilizando Pyhon
# FastAPI Archetype Backend

Arquetipo backend profesional utilizando:

* FastAPI
* PostgreSQL
* SQLAlchemy
* Neon PostgreSQL
* Pydantic
* Uvicorn

---

# Requisitos

* Python 3.11 o 3.12 recomendado
* pip
* Git

---

# Estructura del proyecto

```text
Proyect/
│
├── core/
│   └── database.py
│
├── models/
│   └── user_model.py
│
├── routers/
│   └── user_router.py
│
├── schemas/
│   └── user_schema.py
│
├── main.py
├── requirements.txt
├── .env
└── venv/
```

---

# Crear entorno virtual

## Windows PowerShell

```powershell
python -m venv venv
```

---

# Activar entorno virtual

## Windows PowerShell

```powershell
.\venv\Scripts\Activate
```

---

# Instalar dependencias

```powershell
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

---

# Generar requirements.txt

```powershell
pip freeze > requirements.txt
```

---

# Instalar dependencias desde requirements

```powershell
pip install -r requirements.txt
```

---

# Configurar variables de entorno

Crear archivo:

```text
.env
```

Contenido:

```env
DATABASE_URL=postgresql://USER:PASSWORD@HOST/DATABASE?sslmode=require
```

Ejemplo con Neon:

```env
DATABASE_URL=postgresql://neondb_owner:PASSWORD@ep-example.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

---

# Ejecutar servidor

```powershell
python -m uvicorn main:app --reload
```

---

# Swagger Documentation

Abrir:

```text
http://127.0.0.1:8000/docs
```

---

# Endpoints CRUD

## Obtener usuarios

```http
GET /users
```

---

## Obtener usuario por ID

```http
GET /users/{id}
```

---

## Crear usuario

```http
POST /users
```

Body:

```json
{
  "name": "Paranois",
  "email": "paranois@test.com"
}
```

---

## Actualizar usuario

```http
PUT /users/{id}
```

---

## Eliminar usuario

```http
DELETE /users/{id}
```

---

# Dependencias utilizadas

| Librería        | Uso                  |
| --------------- | -------------------- |
| FastAPI         | Framework backend    |
| Uvicorn         | Servidor ASGI        |
| SQLAlchemy      | ORM                  |
| psycopg2-binary | Driver PostgreSQL    |
| python-dotenv   | Variables de entorno |

---

# Comandos útiles

## Ver paquetes instalados

```powershell
pip freeze
```

---

## Desactivar entorno virtual

```powershell
deactivate
```

---

## Eliminar caché Python

```powershell
Get-ChildItem -Recurse -Directory __pycache__ | Remove-Item -Recurse -Force
```

---

# Buenas prácticas implementadas

* Arquitectura modular
* Separación por capas
* Uso de schemas con Pydantic
* ORM con SQLAlchemy
* Variables de entorno
* CRUD REST
* PostgreSQL remoto con Neon
* Swagger automático

---

# Próximas mejoras recomendadas

* JWT Authentication
* Alembic Migrations
* Docker
* Docker Compose
* Repository Pattern
* Services Layer
* Middleware
* Logging
* Tests automáticos
* CI/CD con GitHub Actions

---

# Stack Tecnológico

* FastAPI
* PostgreSQL
* Neon
* SQLAlchemy
* Python
* Pydantic
* Uvicorn
