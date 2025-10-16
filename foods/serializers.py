from rest_framework import serializers
from .models import Food, Category, Ingredient, FoodIngredient
from ratings.models import Rating

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
    
class MyRatingsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='food.title', read_only=True)
    imgUrl = serializers.CharField(source='food.imgUrl', read_only=True)
    date = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = ['title', 'imgUrl', 'rating', 'date']

    def get_date(self, obj):
        return obj.timestamp.strftime("%d/%m/%Y") if obj.timestamp else ""

class FoodWithRatingSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ['id', 'title', 'imgUrl', 'rating', 'date']

    def _get_rating_obj(self, obj):
        # ratings_map expected to be keyed by Food instances (r.food)
        return self.context.get('ratings_map', {}).get(obj)

    def get_rating(self, obj):
        rating_obj = self._get_rating_obj(obj)
        return rating_obj.rating if rating_obj else 0

    def get_date(self, obj):
        rating_obj = self._get_rating_obj(obj)
        if rating_obj and getattr(rating_obj, 'timestamp', None):
            return rating_obj.timestamp.strftime('%d/%m/%Y')
        return ''