from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class ProfesorAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('apellido','nombre','dni')
        }),
    )
    search_fields = ['apellido','dni']
    list_display = ['apellido','nombre','dni','cursos' ]
    list_display_links = ['apellido','nombre','dni','cursos']

class AlumnoAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('apellido','nombre','dni','curso','user')
        }),
    )
    search_fields = ['apellido','dni']
    list_display = ['apellido','nombre','dni','curso']
    list_display_links = ['apellido','nombre','dni','curso']

class LibroEnVentaAdmin (admin.ModelAdmin):
    list_display = ('titulo','materia', 'descripcion')

class PersonaAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Datos', {
            'fields': ('user','tipo','dni')
        }),
    )

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
admin.site.register (Alumno,AlumnoAdmin,)
admin.site.register (Profesor,ProfesorAdmin,)
admin.site.register (Curso,CursoAdmin,) 
admin.site.register (Persona,PersonaAdmin,) 