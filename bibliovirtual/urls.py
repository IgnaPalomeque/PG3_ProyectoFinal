from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
from .views import registerView, homeView, logoutView, accountView, clase1View, profesoresHomeView,materialDescargableView,materialesSubidosView, venderLibroView, compraLibroView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/register/',registerView,name="register_url"),
    path('accounts/login/',LoginView.as_view(),name="login_url"),
    path('',homeView,name="home_url"),
    path('accounts/logout',logoutView,name="logout_url"),
    path('accounts/account',accountView,name="account_url"),
    path('clases/clase1', clase1View, name="clase1_url"),
    path('profesores/home',profesoresHomeView, name="profesores_home_url"),
    path('clases/material_descargable',materialDescargableView, name="material_descargable_url"),
    path('profesores/materiales_subidos',materialesSubidosView, name="materiales_subidos_url"),
    path('clases/compra_libros', compraLibroView, name="compra_libro_url"),
    path('clases/vender_libro',venderLibroView, name="vender_libro_url")
]
