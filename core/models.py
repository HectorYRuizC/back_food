from django.db import models
from django.contrib.auth.models import AbstractUser


# -------------------
# Users
# -------------------
class User(AbstractUser):
    email = models.EmailField(unique=True)
    creation_date = models.DateField(auto_now_add=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username


# -------------------
# Categories
# -------------------
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# -------------------
# Foods
# -------------------
class Food(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="foods", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# -------------------
# Ingredients
# -------------------
class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# -------------------
# Food - Ingredients (N:M)
# -------------------
class FoodIngredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food.title} - {self.ingredient.name}"


# -------------------
# Ratings
# -------------------
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rated {self.food.title} = {self.rating}"


# -------------------
# Recommendation session
# -------------------
class RecommendationSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessions")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} - {self.user.username}"


# -------------------
# Items inside a session
# -------------------
class SessionItem(models.Model):
    session = models.ForeignKey(RecommendationSession, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session {self.session.id} - {self.food.title}"
