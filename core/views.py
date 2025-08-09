from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Food, Rating, RecommendationHistory
from .serializers import (
    RegisterSerializer, FoodSerializer,
    RatingSerializer, RecommendationHistorySerializer
)
from django.contrib.auth import get_user_model
import random

User = get_user_model()

# Registro de usuario
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# 5 comidas aleatorias
class RandomFoodsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        foods = list(Food.objects.all())
        random_foods = random.sample(foods, min(len(foods), 5))

        # Guardar en historial si el modelo tiene el campo `food`
        for food in random_foods:
            RecommendationHistory.objects.create(user=request.user, food=food)

        serializer = FoodSerializer(random_foods, many=True)
        return Response(serializer.data)

# Crear calificación
class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Historial de recomendaciones
class RecommendationHistoryView(generics.ListAPIView):
    serializer_class = RecommendationHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RecommendationHistory.objects.filter(user=self.request.user)
