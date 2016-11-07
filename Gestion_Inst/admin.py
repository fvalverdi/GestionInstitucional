from django.contrib import admin

# Register your models here.
from .models import Sexo,Alumno,Nivel

admin.site.register(Sexo)
admin.site.register(Alumno)
admin.site.register(Nivel)
