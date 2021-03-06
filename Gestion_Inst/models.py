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
	def __str__(self):
		return self.descripcion

class Curso(models.Model):
	descripcion = models.CharField(max_length=50)
	#nivel = models.ForeignKey(Nivel)
	def __str__(self):
		return self.descripcion

class Division(models.Model):
	descripcion = models.CharField(max_length=50)
	#curso = models.ForeignKey(Curso)
	def __str__(self):
		return self.descripcion

class Alumno(Persona):
	fecha_inicio = models.DateField(default=timezone.now)
	legajo = models.IntegerField(null=True,blank=True)
	estado = models.BooleanField("Activo",default=False) #False significa Inactivo - Activo
	#situacion = models.BooleanField("Moroso",default=False) #False significa Al dia - True Moroso
	nivel = models.ForeignKey(Nivel,null=True)
	curso = models.ForeignKey(Curso,null=True)
	division = models.ForeignKey(Division,null=True)
	def __str__(self):
		return str(self.dni) +' '+self.nombres +' '+self.apellido

class Ciclo(models.Model):
	anio = models.IntegerField()
	monto_cuota = models.FloatField()
	monto_inscripcion = models.FloatField()
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	recargo = models.FloatField()
	def __str__(self):
		return str(self.anio)

class Tipo(models.Model):#Ingresos o Egresos
	descripcion = models.CharField(max_length=50)
	def __str__(self):
		return self.descripcion

class Categoria(models.Model): #puede ser matriculacion, cuota, insumos, compras
	descripcion = models.CharField(max_length=50)
	tipo = models.ForeignKey(Tipo)
	def __str__(self):
		return self.descripcion+' - '+self.tipo.descripcion

class Pagos_Alumnos(models.Model):
	fecha_pago = models.DateTimeField(null=True,blank=True) #(default=timezone.now)
	fecha_inicio = models.DateField(null=True,blank=True)
	fecha_vencimiento = models.DateField(null=True,blank=True)
	monto_abonado = models.FloatField(null=True,blank=True)
	estado = models.BooleanField("Adeuda?",default=False) #False significa Al dia - True= queda saldo pendiente
	alumno = models.ForeignKey(Alumno)
	ciclo = models.ForeignKey(Ciclo)
	categoria = models.ForeignKey(Categoria)

class Ingresos(models.Model):
	fecha_pago = models.DateTimeField(default=timezone.now)
	descripcion = models.CharField(max_length=50)
	categoria = models.ForeignKey(Categoria)
	monto = models.FloatField()

class Egresos(models.Model):
	fecha_pago = models.DateTimeField(default=timezone.now)
	descripcion = models.CharField(max_length=60)
	categoria = models.ForeignKey(Categoria)
	monto = models.FloatField()
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
