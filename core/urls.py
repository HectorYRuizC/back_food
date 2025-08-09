from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, RandomFoodsView, RatingCreateView, RecommendationHistoryView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('foods/random/', RandomFoodsView.as_view(), name='random-foods'),
    path('ratings/', RatingCreateView.as_view(), name='rate-food'),
    path('recommendations/history/', RecommendationHistoryView.as_view(), name='recommendation-history'),
]
