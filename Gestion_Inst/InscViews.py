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
from Gestion_Inst.models import Pagos_Alumnos, Categoria, Alumno



class InscripcionForm(forms.ModelForm):

    class Meta:
        model = Pagos_Alumnos
        fields = ('monto_abonado','estado',)

    def __init__(self,*args,**kwargs):
        super(InscripcionForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Pagos_Alumnos
        fields = ('ciclo',)

    def __init__(self,*args,**kwargs):
        super(MatriculaForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def inscripciones_list(request, alumno, template_name='Gestion_Inst/Inscripcion/inscripcion_list.html'):
    categoria = Categoria.objects.filter(descripcion__icontains='Matricula').get()
    alumno = get_object_or_404(Alumno, pk=alumno)
    inscripciones = Pagos_Alumnos.objects.filter(categoria=categoria.pk).filter(alumno=alumno.pk)
    data = {}
    data['inscripciones'] = inscripciones
    data['alumno'] = alumno
    return render(request, template_name, data)

def inscripciones_create(request, template_name='Gestion_Inst/Inscripcion/inscripcion_form.html'):
    form = MatriculaForm(request.POST or None)
    if form.is_valid():
        #antes de guardar, debo extraer el ciclo selecionado buscarlo  traer todos los datos para crear
        #el registro de la matricula mas las cuotas de pago
        form.save()
        return redirect('inscripciones_list')
    return render(request, template_name, {'form':form})

def inscripciones_update(request, pk, template_name='Gestion_Inst/Inscripcion/inscripcion_form.html'):
    server = get_object_or_404(Pagos_Alumnos, pk=pk)
    form = InscripcionForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('inscripciones_list')
    return render(request, template_name, {'form':form})

def inscripciones_borrar(request, pk):
    server = get_object_or_404(Pagos_Alumnos, pk=pk)

    server.delete()
    return redirect('inscripciones_list')