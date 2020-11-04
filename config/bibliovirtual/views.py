from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def homepage (request):
    return render (request, 'bibliovirtual/homepage.html' , {'name': request.user,})