from django.contrib import admin

# Register your models here.
from .models import Sexo,Alumno

admin.site.register(Sexo)
admin.site.register(Alumno)
