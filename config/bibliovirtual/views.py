from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *

# Create your views here.

def homeView(request):
    alumno = Alumno.objects.only('nombre')
    if request.user.is_authenticated:
        return render (request, 'bibliovirtual/home.html', {'alumno':alumno})
    else:
        return redirect("login_url")

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
    
def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login_url")

def accountView(request):

    return render(request, "bibliovirtual/account.html",)

def alumnooprofesor(request):
    user = User.objects.last()
    persona = Persona.objects.last()

    if user.persona.tipo == "Profesor":
        return render (request, 'bibliovirtual/home.html')
    else:
        return render(request, 'registration/register.html')