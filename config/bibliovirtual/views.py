from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.

def login (request):
    return render (request, 'bibliovirtual/login.html')
    