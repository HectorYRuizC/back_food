from rest_framework.routers import DefaultRouter
from .views import SessionViewSet, user_packs
from django.urls import include, path


router = DefaultRouter()
router.register("sessions", SessionViewSet, basename="sessions")
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('packs/', user_packs, name='user-packs'),
]