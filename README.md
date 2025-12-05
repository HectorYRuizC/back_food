# 🧩 Proyecto Django REST + Docker + PostgreSQL

Este proyecto es una API construida con **Django REST Framework**, usando **PostgreSQL** como base de datos y **Docker** para entorno aislado y reproducible.

---

# 📌 Requisitos previos

Antes de correr el proyecto por primera vez, asegúrate de tener instalado:

### ✅ Obligatorio (si usarás Docker)
- **Docker**  
  https://docs.docker.com/get-docker/
- **Docker Compose**  
  https://docs.docker.com/compose/install/

### 🧪 Opcional (si quieres correrlo sin Docker)
- **Python 3.10+**
- **pip**
- **Virtualenv** 

---

# 🚀 Cómo correr el proyecto por primera vez (CON DOCKER)

Este es el flujo recomendado porque no requiere instalar Python ni Postgres localmente.

### ▶️ 1. Construir y levantar los contenedores (primera vez)
# Construye la imagen y levanta el entorno por primera vez
docker-compose up --build

### ▶️ 2. Aplicar las migraciones de Django
# Crea las tablas en la base de datos
docker-compose exec web python manage.py migrate

### ▶️ 3. Insertar datos de prueba (seeds)
# Inserta datos de alimentos de ejemplo
docker-compose exec web python manage.py seed_foods
# Inserta usuarios y ratings de ejemplo
docker-compose exec web python.manage.py seed_users_and_ratings

### ▶️ 4. Crear un usuario administrador
# Crear superusuario para acceder a /admin
docker-compose exec web python.manage.py createsuperuser

### ▶️ 5. Levantar el proyecto normalmente después de la primera vez
# Levanta el proyecto sin reconstruir imágenes
docker-compose up