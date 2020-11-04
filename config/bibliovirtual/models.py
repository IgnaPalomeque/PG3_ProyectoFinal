from django.db import models

# Create your models here.


class Curso (models.Model):
    anios = [
        ("1","1 año"), 
        ("2","2 año"),
        ("3","3 año"),
        ("4","4 año"), 
        ("5","5 año"),
        ("6","6 año"),
        ("7","7 año"),
    ]
    anio = models.CharField(max_length= 10,choices = anios, null=True)
    divisiones = [
        ("°A","°A"), 
        ("°B","°B"),
        ("°C","°C"),
    ]
    division = models.CharField(max_length= 10,choices = divisiones)

    def __str__(self):
        temp = (str(self.anio) + str(self.division))
        return temp

class Persona (models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 10)
    apellido = models.CharField(max_length= 10)
    contraseña = models.CharField(max_length= 20)

class Alumno (Persona):
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, null=True,)

    def __str__(self):
        temp = (str(self.apellido)+ " " + str(self.nombre))
        return temp


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

class MateriaDescargable (Material):
    # pdf = models.FileFields(upload_to='pdfdescarga/')
    pass

class LibroEnVenta (Material):
    vendedor = models.ForeignKey('Alumno', on_delete=models.CASCADE, null=True,)
    descripcion = models.CharField(max_length= 200)
