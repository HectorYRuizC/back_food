from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE, related_name="user_rol", null=True)


    REQUIRED_FIELDS = ["email"]
    def __str__(self):
        return self.username