from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Endpoint to obtain access and refresh tokens
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Endpoint to refresh access token using refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
