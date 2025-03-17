from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth import views
from rest_framework import urls

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name="user_register"),
    path('login/', views.LoginView.as_view(), name="user_login"),
    path('logout/', views.LogoutView.as_view(), name="user_logout"),
]