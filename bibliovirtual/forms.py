from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import MaterialDescargable, LibroEnVenta



class registerForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name',)

class uploadMaterial(ModelForm):
    class Meta:
        model = MaterialDescargable
        fields = ('curso', 'materia', 'titulo', 'descripcion', 'pdf')

class uploadLibro (ModelForm):
    class Meta:
        model = LibroEnVenta
        fields = ('curso', 'materia', 'titulo', 'descripcion', 'foto_portada')

class venderLibroForm(ModelForm):
    class Meta:
        model = LibroEnVenta
        fields = ('vendedor','materia', 'titulo', 'curso', 'descripcion','foto_portada')