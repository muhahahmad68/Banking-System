from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.RegisterView, name='sign-up'),
    path('sign-in/', views.LoginView, name='sign-in'),
    path('sign-out/', views.LogoutView, name='sign-out'),
]

