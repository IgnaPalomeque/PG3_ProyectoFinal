from django.db import models

# Create your models here.


class Curso (models.Model):
    divisiones = [
        ("A","A"), 
        ("B","B"),
        ("C","C"),
    ]
    division = models.CharField(max_length= 1, choices = divisiones,)

class Persona (models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 10)
    apellido = models.CharField(max_length= 10)
    contraseña = models.CharField(max_length= 20)

class Alumno (Persona):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True,)

class Profesor (Persona):
    cursos = []

class Materia (models.Model):
    titulo = models.CharField(max_length= 20)
    
class Material (models.Model):
    materias = [
        ("L","Lengua"), 
        ("B", "Biologia"),
        ("M", "Matematica"),
        ("I", "Ingles"),
        ("P", "Programacion"),
    ]
    materia = models.CharField(max_length= 20,choices = materias)
    titulo = models.CharField(max_length= 20,primary_key=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True,)
    descripcion = models.CharField(max_length= 200, default = " ")
    

class MateriaDescargable (Material):
    pdf = models.FileField(max_length=100,upload_to='pdfdescarga/', blank=True)

class LibroEnVenta (Material):
    vendedor = models.ForeignKey('Alumno', on_delete=models.CASCADE, null=True,)
    foto_portada = models.ImageField(max_length=100, upload_to='fotos_portada/', blank=True)
    
