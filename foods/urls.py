from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, CategoryViewSet, IngredientViewSet, AllFoodsView, FoodWithRatingsView
from django.urls import path, include

router = DefaultRouter()
router.register("items", FoodViewSet, basename="foodstest")
router.register("categories", CategoryViewSet, basename="categories")
router.register("ingredients", IngredientViewSet, basename="ingredients")


urlpatterns = [
    path('',include(router.urls)),
    path('foods',AllFoodsView.as_view()),
    path('ratings/', FoodWithRatingsView.as_view(), name='food-ratings'),
]
