from django.urls import path,include
from django.contrib.auth.views import LoginView
from .views import register
from .views import home

urlpatterns = [
    path('',register),
    path('login',LoginView.as_view(),name="login_url"),
    path('home',home)
    path('prueba',profesoroalumno, name="prueba_url"),
]
