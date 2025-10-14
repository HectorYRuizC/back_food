from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from django_filters.rest_framework import FilterSet, filters
from rest_framework.response import Response
from .models import Food, Category, Ingredient
from .serializers import FoodSerializer, CategorySerializer, IngredientSerializer, FoodWithRatingSerializer
from core.permissions import IsStaffOrReadOnly
from ratings.models import Rating



class AllFoodsView(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FoodWithRatingsView(generics.ListAPIView):
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FoodWithRatingSerializer
    queryset = Food.objects.all()

    def get_queryset(self):
        user = self.request.user
        # preload all ratings for this user and select_related the food
        user_ratings = Rating.objects.filter(user=user).select_related('food')
        # map by Food instance (r.food)
        self.ratings_map = {r.food: r for r in user_ratings}
        return super().get_queryset()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['ratings_map'] = getattr(self, 'ratings_map', {})
        return context


###################################

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
