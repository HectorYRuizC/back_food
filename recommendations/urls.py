from rest_framework.routers import DefaultRouter
from .views import SessionViewSet, last_recommendations, recommendation_packs
from django.urls import include, path



router = DefaultRouter()
router.register("sessions", SessionViewSet, basename="sessions")
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('packs', recommendation_packs, name='user-packs'),
    path('last/', last_recommendations, name='last-recommendations'),
]