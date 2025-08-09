from rest_framework import serializers
from .models import User, Food, Rating, RecommendationHistory
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'ingredients']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'food', 'rating', 'timestamp']
        read_only_fields = ['user', 'timestamp']

class RecommendationHistorySerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.name', read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = RecommendationHistory
        fields = ['food_name', 'created_at', 'rating']

    def get_rating(self, obj):
        user = obj.user
        food = obj.food
        rating = Rating.objects.filter(user=user, food=food).first()
        return rating.rating if rating else "No calificado"
