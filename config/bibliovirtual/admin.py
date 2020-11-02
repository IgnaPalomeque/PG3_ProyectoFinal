from django.contrib import admin
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
            'fields': ('apellido','nombre','dni','curso')
        }),
    )
    search_fields = ['apellido','dni']
    list_display = ['apellido','nombre','dni','curso']
    list_display_links = ['apellido','nombre','dni','curso']

class LibroEnVentaAdmin (admin.ModelAdmin):
    list_display = ('titulo','materia', 'descripcion')

class MateriaDescargableAdmin (admin.ModelAdmin):
    list_display = ('titulo','materia',)

admin.site.register (MateriaDescargable,MateriaDescargableAdmin,)
admin.site.register (LibroEnVenta,LibroEnVentaAdmin,)
admin.site.register (Alumno,AlumnoAdmin,)
admin.site.register (Profesor,ProfesorAdmin,)