# Imagen base oficial de Python
from python:3.13-slim


# Evita que Python guarde archivos .pyc y buffers
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear directorio de la app
WORKDIR /app

# Instalar dependencias del sistema (ej: para psycopg2 si usas Postgres)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements si existe
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto
COPY . /app/

# Exponer el puerto
EXPOSE 8000

# Comando para correr el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
