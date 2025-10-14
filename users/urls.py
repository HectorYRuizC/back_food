from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, MeView, LoginView, UserProfileView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),           
    path("token", LoginView.as_view(), name="token_obtain"),  
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("me", MeView.as_view(), name="me"), #jwt needed             
    path('profile', UserProfileView.as_view(), name='user-profile'),    
]
