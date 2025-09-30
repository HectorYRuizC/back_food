from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Documentación OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),

    # Autenticación y usuarios
    path("api/auth/", include("users.urls")),

    # Foods
    path("api/foods/", include("foods.urls")),

    # Ratings
    path("api/ratings/", include("ratings.urls")),

    # Recomendaciones
    path("api/recommendations/", include("recommendations.urls")),
]
