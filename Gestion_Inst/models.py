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
	fecha_nac = models.DateField(null=True,blank=True)
	domicilio = models.CharField(max_length=200, null=True,blank=True)
	telefono = models.CharField(max_length=15, null=True,blank=True)
	dni = models.IntegerField()
	sexo = models.ForeignKey(Sexo)
	def __str__(self):
		return str(self.dni) +' '+self.nombres +' '+self.apellido

class Nivel(models.Model):
	descripcion = models.CharField(max_length=50)

class Curso(models.Model):
	descripcion = models.CharField(max_length=50)
	nivel = models.ForeignKey(Nivel)

class Division(models.Model):
	descripcion = models.CharField(max_length=50)
	curso = models.ForeignKey(Curso)

class Alumno(Persona):
	fecha_inicio = models.DateField(default=timezone.now)
	legajo = models.IntegerField(null=True,blank=True)
	estado = models.BooleanField(default=False) #False significa Inactivo - Activo
	division = models.ForeignKey(Division)

class Ciclo(models.Model):
	anio = models.IntegerField()
	monto_cuota = models.FloatField()
	monto_inscripcion = models.FloatField()
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	recargo = models.FloatField()

class Categoria(models.Model):
	descripcion = models.CharField(max_length=50)
	tipo = models.BooleanField()

class Pagos_Alumnos(models.Model):
	fecha_pago = models.DateTimeField(default=timezone.now)
	fecha_inicio = models.DateField()
	fecha_vencimiento = models.DateField()
	monto_abonado = models.FloatField()
	estado = models.BooleanField()
	alumno = models.ForeignKey(Alumno)
	ciclo = models.ForeignKey(Ciclo)
	categoria = models.ForeignKey(Categoria)

class Ingresos(models.Model):
	fecha_pago = models.DateTimeField(default=timezone.now)
	descripcion = models.CharField()
	categoria = models.ForeignKey(Categoria)

class Egresos(models.Model):
	fecha_pago = models.DateTimeField(default=timezone.now)
	descripcion = models.CharField()
	categoria = models.ForeignKey(Categoria)

# 	curso = models.ForeignKey(Curso)
#
# class Curso(models.Model):
#     anio = models.CharField()
#     division = models.CharField()
#
# class Egresos(models.Model):
#     descripcion = models.CharField()
#     fecha = models.DateField()
#     monto = models.FloatField()
