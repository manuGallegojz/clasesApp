from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=40)
    email=models.EmailField()
    telefono=models.IntegerField()
    dni=models.IntegerField()

class Clase(models.Model):
    fecha=models.DateField(max_length=40)
    materia=models.CharField(max_length=80)
    tema=models.CharField(max_length=80)
