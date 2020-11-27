from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import MaterialDescargable



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
        fields = ('materia', 'titulo', 'curso', 'descripcion', 'pdf')