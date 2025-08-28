from rest_framework import serializers
from .models import User, Category, Food, Ingredient, FoodIngredient, Rating, RecommendationSession, SessionItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "creation_date"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class FoodIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIngredient
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Food
        fields = ["id", "title", "category", "ingredients"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class RecommendationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationSession
        fields = "__all__"


class SessionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionItem
        fields = "__all__"
