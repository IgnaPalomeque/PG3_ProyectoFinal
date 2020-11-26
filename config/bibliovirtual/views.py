from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from .models import *
from .forms import *

# Create your views here.

def homeView(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='profesores').exists():
            return render (request, 'bibliovirtual/profesores_home.html')
        else:
            return render (request, 'bibliovirtual/home.html')
    else:
        return redirect("login_url")

def registerView(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = registerForm()

    return render(request, 'registration/register.html', {'form': form})
    
def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login_url")

def accountView(request):

    return render(request, "bibliovirtual/account.html",)

def clase1View(request):

    return render(request, 'clases/clase1.html')