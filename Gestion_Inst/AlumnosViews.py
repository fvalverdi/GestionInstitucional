from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response,redirect, get_object_or_404
# Create your views here.
from django.template.context_processors import csrf

#from Gestion_Inst.forms import AlumnoForm,NivelEnsenanzaForm
from Gestion_Inst.models import *
from crispy_forms.bootstrap import StrictButton, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import forms
from django import forms
from Gestion_Inst.models import Alumno

class AlumnoForm(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = ('apellido', 'nombres', 'fecha_nac', 'domicilio', 'telefono', 'dni', 'sexo', 'legajo', 'estado','nivel', 'curso','division','situacion',)

    def __init__(self,*args,**kwargs):
        super(AlumnoForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def alumnos_list(request, template_name='Gestion_Inst/Alumno/alumnos_list.html'):
    servers = Alumno.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def alumno_create(request, template_name='Gestion_Inst/Alumno/alumno_form.html'):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('alumnos_list')
    return render(request, template_name, {'form':form})

def alumno_update(request, pk, template_name='Gestion_Inst/Alumno/alumno_form.html'):
    server = get_object_or_404(Alumno, pk=pk)
    form = AlumnoForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('alumnos_list')
    return render(request, template_name, {'form':form})

def alumno_delete(request, pk, template_name='Gestion_Inst/Alumno/alumno_confirm_delete.html'):
    server = get_object_or_404(Alumno, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('alumno_list')
    return render(request, template_name, {'object':server})