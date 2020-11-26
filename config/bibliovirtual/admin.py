from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class LibroEnVentaAdmin (admin.ModelAdmin):
    list_display = ('titulo','materia', 'descripcion')

class MateriaDescargableAdmin (admin.ModelAdmin):
    fieldsets = (
            ('Información material', {
                'fields': (
                    'titulo', 'materia', 'curso',
                ),
            }),
            ('Informacion extra', {
                'fields': (
                    'foto_portada', 'descripcion',
                ),
            }),
        )
class CursoAdmin (admin.ModelAdmin):
    list_display = ('anio','division',)

admin.site.register (MateriaDescargable,MateriaDescargableAdmin,)
admin.site.register (LibroEnVenta,LibroEnVentaAdmin,)
admin.site.register (Curso,CursoAdmin,) 