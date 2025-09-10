from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, CategoryViewSet, IngredientViewSet

router = DefaultRouter()
router.register("items", FoodViewSet, basename="foods")
router.register("categories", CategoryViewSet, basename="categories")
router.register("ingredients", IngredientViewSet, basename="ingredients")

urlpatterns = router.urls
