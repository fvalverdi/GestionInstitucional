from django.forms import forms
from django import forms
from Gestion_Inst.models import Alumno


class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('apellido', 'nombres','fecha_nac','domicilio','telefono','dni','sexo','legajo','estado')