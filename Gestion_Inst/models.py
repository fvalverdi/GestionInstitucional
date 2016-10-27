from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Sexo(models.Model):
	descripcion = models.CharField(max_length=15)
	def __str__(self):
		return self.descripcion

class Persona(models.Model):
	apellido = models.CharField(max_length=50)
	nombres = models.CharField(max_length=100)
	fecha_nac = models.DateField()
	domicilio = models.CharField(max_length=200)
	telefono = models.CharField(max_length=15)
	dni = models.IntegerField()
	sexo = models.ForeignKey(Sexo)
	def __str__(self):
		return str(self.dni) +' '+self.nombres +' '+self.apellido

class Alumno(Persona):
	fecha_inicio = models.DateTimeField(default=timezone.now)
	legajo = models.IntegerField()
	estado = models.CharField(max_length=50)
	curso = models.ForeignKey(Curso)

class Curso(models.Model):
    anio = models.CharField()
    division = models.CharField()

class Egresos(models.Model)
    descripcion = models.CharField()
    fecha = models.DateField()
    monto = models.FloatField()
