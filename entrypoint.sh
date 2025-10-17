#!/bin/bash
set -e

echo "📦 Aplicando migraciones..."
python manage.py migrate

echo "🍔 Insertando datos iniciales..."
python manage.py seed_foods || echo "⚠️ seed_foods no disponible"
python manage.py seed_users_and_ratings || echo "⚠️ seed_users_and_ratings no disponible"

echo "🎨 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "🚀 Iniciando servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
