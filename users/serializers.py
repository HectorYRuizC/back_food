from rest_framework import serializers
from foods.models import Food
from ratings.models import Rating
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Notice we authenticate with `username=email`
        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id, # type: ignore[attr-defined]
                "username": user.username,
                "email": user.email,
            },
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_superuser", "created_at"]
        read_only_fields = ["id", "is_staff", "is_superuser", "created_at"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User(username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    total_rated_foods = serializers.SerializerMethodField()
    rating_average = serializers.SerializerMethodField()
    favorite_meal = serializers.SerializerMethodField()
    least_favorite_meal = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'created_at',
            'total_rated_foods',
            'rating_average',
            'favorite_meal',
            'least_favorite_meal'
        ]

    def get_created_at(self, obj):
        # Format as dd/mm/yyyy
        return obj.created_at.strftime("%d/%m/%Y") if obj.created_at else None

    def get_total_rated_foods(self, obj):
        return Rating.objects.filter(user=obj).count()

    def get_rating_average(self, obj):
        from django.db.models import Avg
        avg_rating = Rating.objects.filter(user=obj).aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 2) if avg_rating is not None else 0

    def get_favorite_meal(self, obj):
        ratings = Rating.objects.filter(user=obj).select_related('food')
        if not ratings.exists():
            return {
                "exist": False,
                "title": "No foods rated yet",
                "url_photo": "https://non-existing",
                "rating": 0
            }
        top_rating = ratings.order_by('-rating', 'id').first()
        if not top_rating or not top_rating.food:
            return {
                "exist": False,
                "title": "No foods rated yet",
                "url_photo": "https://non-existing",
                "rating": 0
            }
        return {
            "exist": True,
            "title": top_rating.food.title,
            "url_photo": top_rating.food.imgUrl,
            "rating": top_rating.rating
        }
    
    def get_least_favorite_meal(self, obj):
        ratings = Rating.objects.filter(user=obj).select_related('food')
        # No ratings at all
        if not ratings.exists():
            return {
                "exist": False,
                "title": "No foods rated yet",
                "url_photo": "https://non-existing",
                "rating": 0
            }
        # Only one rating → same as favorite
        if ratings.count() == 1:
            only = ratings.first()
            if not only or not only.food:
                return {
                    "exist": False,
                    "title": "No foods rated yet",
                    "url_photo": "https://non-existing",
                    "rating": 0
                }
            return {
                "exist": True,
                "title": only.food.title,
                "url_photo": only.food.imgUrl,
                "rating": only.rating
            }
        # Get lowest-rated food
        low_rating = ratings.order_by('rating', 'id').first()
        # Safety check for Pylance and unexpected nulls
        if not low_rating or not low_rating.food:
            return {
                "exist": False,
                "title": "No foods rated yet",
                "url_photo": "https://non-existing",
                "rating": 0
            }
        return {
            "exist": True,
            "title": low_rating.food.title,
            "url_photo": low_rating.food.imgUrl,
            "rating": low_rating.rating
        }