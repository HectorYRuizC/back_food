import csv, random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from foods.models import Food
from ratings.models import Rating
from django.db import transaction

User = get_user_model()

class Command(BaseCommand):
    help = "Carga usuarios y calificaciones desde ratings/datos/datos.csv con nombres realistas"

    @transaction.atomic
    def handle(self, *args, **options):
        file_path = "ratings/datos/datos.csv"

        try:
            with open(file_path, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                data = list(reader)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"❌ No se encontró el archivo: {file_path}"))
            return

        # Listas base de nombres
        first_names = [
            "Juan", "Pedro", "María", "Laura", "Andrés", "Camila", "Diego", "Ana",
            "Sofía", "Daniel", "Carolina", "Luis", "Valentina", "Julián", "Paula",
            "David", "Fernanda", "Santiago", "Isabella", "Nicolás", "Luisa", "Jorge",
            "Adriana", "Sebastián", "Natalia", "Felipe", "Gabriela", "Ricardo", "Manuela",
            "José", "Verónica", "Cristian", "Claudia", "Esteban", "Andrea", "Mauricio",
            "Catalina", "Héctor", "Marcela", "Óscar", "Patricia", "Tomás", "Liliana",
            "Alejandro", "Mónica", "Samuel", "Lorena", "Emilio", "Daniela", "Fernando",
            "Lucía", "Hernán", "Elena", "César", "Juliana", "Miguel", "Sandra",
            "Pablo", "Ximena", "Iván", "Tatiana", "Camilo", "Gloria", "Rafael",
            "Karina", "Gustavo", "Yesenia", "Eduardo", "Carmen", "Simón", "Raúl"
        ]

        # Mezclar aleatoriamente y tomar los primeros 70 nombres únicos
        random.shuffle(first_names)
        selected_names = first_names[:70]

        users = []
        for i, name in enumerate(selected_names, start=1):
            username = name.lower()
            email = f"{username}{i}@example.com"
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password("12345678")
                user.save()
            users.append(user)

        self.stdout.write(self.style.SUCCESS(f"✅ {len(users)} usuarios creados o verificados con nombres realistas."))

        # Crear calificaciones
        ratings_created = 0
        for row in data:
            try:
                user_id = int(row["id_usuario"])
                food_id = int(row["id_comida"])
                rating_value = int(row["clasificacion"])

                user = users[user_id - 1]
                food = Food.objects.filter(id=food_id).first()
                if not food:
                    continue

                _, created = Rating.objects.get_or_create(
                    user=user,
                    food=food,
                    defaults={"rating": rating_value}
                )
                if created:
                    ratings_created += 1
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"⚠️ Error con fila {row}: {e}"))
                continue

        self.stdout.write(self.style.SUCCESS(f"⭐ {ratings_created} calificaciones creadas exitosamente"))
