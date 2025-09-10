from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self): return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self): return self.name

class Food(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="foods")
    ingredients = models.ManyToManyField(Ingredient, through="FoodIngredient", related_name="foods")

    def __str__(self): return self.title

class FoodIngredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("food", "ingredient")
