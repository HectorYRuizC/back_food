from django.contrib import admin
from .models import Category, Ingredient, Food, FoodIngredient

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Food)
admin.site.register(FoodIngredient)
