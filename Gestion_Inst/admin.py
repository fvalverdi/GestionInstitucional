from django.contrib import admin

# Register your models here.
from .models import Sexo,Alumno,Nivel,Tipo

admin.site.register(Sexo)
admin.site.register(Alumno)
admin.site.register(Nivel)
admin.site.register(Tipo)
