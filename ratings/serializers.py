from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "user", "food", "rating", "timestamp"]
        read_only_fields = ["id", "user", "timestamp"]

    def validate_rating(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("rating debe ser entre 1 y 5")
        return value

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
