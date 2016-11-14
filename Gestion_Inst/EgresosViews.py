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
from Gestion_Inst.models import Egresos



class EgresosForm(forms.ModelForm):

    class Meta:
        model = Egresos
        fields = ('categoria','fecha_pago','monto','descripcion',)

    def __init__(self,*args,**kwargs):
        super(EgresosForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def egresos_list(request, template_name='Gestion_Inst/Egresos/egresos_list.html'):
    servers = Egresos.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def egreso_create(request, template_name='Gestion_Inst/Egresos/egresos_form.html'):
    form = EgresosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('egresos_list')
    return render(request, template_name, {'form':form})

def egreso_update(request, pk, template_name='Gestion_Inst/Egresos/egresos_form.html'):
    server = get_object_or_404(Ciclo, pk=pk)
    form = EgresosForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('egresos_list')
    return render(request, template_name, {'form':form})

def egreso_borrar(request, pk):
    server = get_object_or_404(Ciclo, pk=pk)

    server.delete()
    return redirect('egresos_list')