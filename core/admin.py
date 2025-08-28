from django.contrib import admin
from .models import (
    User, Category, Food, Ingredient, FoodIngredient,
    Rating, RecommendationSession, SessionItem
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "creation_date")
    search_fields = ("username", "email")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category")
    list_filter = ("category",)
    search_fields = ("title",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(FoodIngredient)
class FoodIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "food", "ingredient")
    list_filter = ("food", "ingredient")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "food", "rating", "fecha")
    list_filter = ("rating",)
    search_fields = ("user__username", "food__title")


@admin.register(RecommendationSession)
class RecommendationSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation_date")
    list_filter = ("creation_date",)


@admin.register(SessionItem)
class SessionItemAdmin(admin.ModelAdmin):
    list_display = ("id", "session", "food")
    list_filter = ("session", "food")
