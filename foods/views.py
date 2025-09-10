from rest_framework import viewsets, permissions
from django_filters.rest_framework import FilterSet, filters
from .models import Food, Category, Ingredient
from .serializers import FoodSerializer, CategorySerializer, IngredientSerializer
from core.permissions import IsStaffOrReadOnly



class FoodFilter(FilterSet):
    category = filters.NumberFilter(field_name="category_id")
    ingredient = filters.NumberFilter(field_name="ingredients__id")

    class Meta:
        model = Food
        fields = ["category", "ingredient", "title"]

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all().select_related("category").prefetch_related("ingredients")
    serializer_class = FoodSerializer
    permission_classes = [IsStaffOrReadOnly]       # pública lectura, staff para escribir
    filterset_class = FoodFilter
    search_fields = ["title", "category__name", "ingredients__name"]
    ordering_fields = ["id", "title"]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["id","name"]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["id","name"]
