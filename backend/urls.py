from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/auth/", include("users.urls")),
    path("api/foods/", include("foods.urls")),
    path("api/ratings/", include("ratings.urls")),
    path("api/recommendations/", include("recommendations.urls")),
]
