FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh

ENV DJANGO_SETTINGS_MODULE=backend.config.settings.prod

ENTRYPOINT ["/app/entrypoint.sh"]


    #CMD ["bash", "-lc", "python manage.py collectstatic --noinput && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

    #CMD ["bash", "-lc", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn backend.wsgi:application --bind 0.0.0.0:8000"]
