from rest_framework import routers
from authuser.views import MyTokenObtainPairView, PublicProfileView, PrivateUserProfileView, UserRegistrationView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer/<int:pk>/', PublicProfileView.as_view(), name='public-profile'),
    path('account/', PrivateUserProfileView.as_view(), name='private-profile'),
]