from rest_framework.routers import DefaultRouter
from .views import RatingViewSet, rate_food
from django.urls import include, path

router = DefaultRouter()
router.register("", RatingViewSet, basename="ratings")


urlpatterns = [
    path("rate/", rate_food, name="rate_food"),
    path('',include(router.urls)),
    
]

