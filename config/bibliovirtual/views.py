from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def home(request):
    return render(request,'bibliovirtual/home.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def profesoroalumno (request):
    alumno = Alumno.objects.only('dni')
    return render (request, 'bibliovirtual/home.html',{'alumno':alumno})
