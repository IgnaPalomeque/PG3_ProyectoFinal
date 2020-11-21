from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
from .views import registerView, homeView, logoutView, accountView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/register/',registerView,name="register_url"),
    path('accounts/login/',LoginView.as_view(),name="login_url"),
    path('',homeView,name="home_url"),
    path('accounts/logout',logoutView,name="logout_url"),
    path('accounts/account',accountView,name="account_url"),
]
