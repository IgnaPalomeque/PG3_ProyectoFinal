from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your models here.


class Alumno (models.Model):     
    user = models.OneToOneField(User, on_delete=models.CASCADE)     
    curso = models.OneToOneField('Curso', on_delete=models.CASCADE, null=True,)

class Curso (models.Model):
    anios = [
        ("1 año","1ero"), 
        ("2","2do"),
        ("3","3ero"),
        ("4","4to"), 
        ("5","5to"),
        ("6","6to"),
        ("7","7mo"),
    ]
    anio = models.CharField(max_length= 10,choices = anios, null=True)
    divisiones = [
        ("A","°A"), 
        ("B","°B"),
        ("C","°C"),
    ]
    division = models.CharField(max_length= 10,choices = divisiones)

    def __str__(self):
        temp = (str(self.anio) + str(self.division))
        return temp

    def get_curso(self):
        temp = self.anio
        return temp
    
    def get_division (self):
        temp = self.division
        return temp

class Material (models.Model):
    materias = [
        ("Lengua","Lengua"), 
        ("Biologia", "Biologia"),
        ("Matematica", "Matematica"),
        ("Ingles", "Ingles"),
        ("Programacion", "Programacion"),
    ]
    materia = models.CharField(max_length= 20,choices = materias)
    titulo = models.CharField(max_length= 100,primary_key=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True,)
    descripcion = models.CharField(max_length= 200, default = "")

    def get_materia(self):
        temp = (str(self.materia))
        return temp
    

class MaterialDescargable (Material):
    pdf = models.FileField(max_length=100,upload_to='pdfdescarga/', blank=True)

    def __str__(self):
        temp = (str(self.titulo) +" "+ str(self.materia) +" "+ str(self.curso))
        return temp

class LibroEnVenta (Material):
    vendedor = models.CharField(max_length= 20,null=True)
    foto_portada = models.ImageField(max_length=100, upload_to='fotos_portada/', blank=True)
    
