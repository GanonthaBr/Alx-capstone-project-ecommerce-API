from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('users/register/',RegisterView.as_view(),name='register'),
    path('users/login/',LoginView.as_view(),name='login'),
    path('profile/',ProfileView.as_view(),name='profile'),
]