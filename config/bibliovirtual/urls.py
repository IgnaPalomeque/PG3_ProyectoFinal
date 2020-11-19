from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
from .views import register, home, profesoroalumno
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',register),
    path('login',LoginView.as_view(),name="login_url"),
    path('home',home),
    path('prueba',profesoroalumno, name="prueba_url"),
]
