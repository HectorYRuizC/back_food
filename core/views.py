from rest_framework import viewsets
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodIngredientViewSet(viewsets.ModelViewSet):
    queryset = FoodIngredient.objects.all()
    serializer_class = FoodIngredientSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RecommendationSessionViewSet(viewsets.ModelViewSet):
    queryset = RecommendationSession.objects.all()
    serializer_class = RecommendationSessionSerializer


class SessionItemViewSet(viewsets.ModelViewSet):
    queryset = SessionItem.objects.all()
    serializer_class = SessionItemSerializer

