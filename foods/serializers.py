from rest_framework import serializers
from .models import Food, Category, Ingredient, FoodIngredient

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]

class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=Category.objects.all(), write_only=True
    )
    ingredients = IngredientSerializer(many=True, read_only=True)
    ingredient_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, source="ingredients", queryset=Ingredient.objects.all()
    )

    class Meta:
        model = Food
        fields = ["id", "title", "category", "category_id", "ingredients", "ingredient_ids"]

    def create(self, validated_data):
        ingredients = validated_data.pop("ingredients", [])
        food = Food.objects.create(**validated_data)
        if ingredients:
            food.ingredients.set(ingredients)
        return food

    def update(self, instance, validated_data):
        ingredients = validated_data.pop("ingredients", None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        if ingredients is not None:
            instance.ingredients.set(ingredients)
        return instance
