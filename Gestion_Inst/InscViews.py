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
from Gestion_Inst.models import Pagos_Alumnos



class IngresosForm(forms.ModelForm):

    class Meta:
        model = Ingresos
        fields = ('categoria','fecha_pago','monto','descripcion',)

    def __init__(self,*args,**kwargs):
        super(IngresosForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def ingresos_list(request, template_name='Gestion_Inst/Ingresos/ingresos_list.html'):
    servers = Ingresos.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def ingreso_create(request, template_name='Gestion_Inst/Ingresos/ingresos_form.html'):
    form = IngresosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ingresos_list')
    return render(request, template_name, {'form':form})

def ingreso_update(request, pk, template_name='Gestion_Inst/Ingresos/ingresos_form.html'):
    server = get_object_or_404(Ciclo, pk=pk)
    form = IngresosForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('ingresos_list')
    return render(request, template_name, {'form':form})

def ingreso_borrar(request, pk):
    server = get_object_or_404(Ciclo, pk=pk)

    server.delete()
    return redirect('ingresos_list')