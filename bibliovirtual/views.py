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
            return redirect ('profesores_home_url')
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

def profesoresHomeView (request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='profesores').exists():
            material = MaterialDescargable.objects.all()
            if request.method == "POST":
                form = uploadMaterial(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect("profesores_home_url")
            else:
                form = uploadMaterial()
            return render(request, 'profesores/profesores_home.html', {'form': form, 'material': material})
            
        else:
            return redirect ('home_url')
    else:
        return redirect("login_url")


def materialDescargableView(request):
    material = MaterialDescargable.objects.all()
    return render(request,"clases/material_descargable.html",{'material':material})


def materialesSubidosView(request):
    material = MaterialDescargable.objects.all()
    if request.user.is_authenticated:
        if request.user.groups.filter(name='profesores').exists():
            return render(request,"profesores/materiales_subidos.html",{'material':material})
        else:
            return redirect ('home_url')
    else:
        return redirect("login_url")
    
def publicarLibroView(request):
    if request.method == "POST":
        form = venderLibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_url")
    else:
        form = venderLibroForm()

    return render(request,"clases/publicar_libro.html",{'form':form})


def comprarLibroView(request):

    libro = LibroEnVenta.objects.all()

    return render(request,"clases/comprar_libro.html",{'libro':libro})



    
