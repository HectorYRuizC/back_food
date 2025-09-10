from rest_framework import serializers
from .models import RecommendationSession, SessionItem
from foods.serializers import FoodSerializer

class SessionItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)

    class Meta:
        model = SessionItem
        fields = ["id", "food"]

class RecommendationSessionSerializer(serializers.ModelSerializer):
    items = SessionItemSerializer(many=True, read_only=True)

    class Meta:
        model = RecommendationSession
        fields = ["id", "user", "created_at", "items"]
        read_only_fields = ["id", "user", "created_at"]

    def create(self, validated_data):
        session = RecommendationSession.objects.create(user=self.context["request"].user, **validated_data)
        return session
