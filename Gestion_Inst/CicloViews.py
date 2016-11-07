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
from Gestion_Inst.models import Ciclo



class CicloForm(forms.ModelForm):

    class Meta:
        model = Ciclo
        fields = ('anio','monto_cuota','monto_inscripcion','fecha_inicio','fecha_fin','recargo',)

    def __init__(self,*args,**kwargs):
        super(CicloForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def ciclo_list(request, template_name='Gestion_Inst/Ciclo/ciclo_list.html'):
    servers = Nivel.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def ciclo_create(request, template_name='Gestion_Inst/Ciclo/ciclo_form.html'):
    form = CicloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ciclo_list')
    return render(request, template_name, {'form':form})

def ciclo_update(request, pk, template_name='Gestion_Inst/Ciclo/ciclo_form.html'):
    server = get_object_or_404(Nivel, pk=pk)
    form = CicloForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('ciclo_list')
    return render(request, template_name, {'form':form})

def ciclo_delete(request, pk, template_name='Gestion_Inst/Ciclo/ciclo_confirm_delete.html'):
    server = get_object_or_404(Nivel, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('ciclo_list')
    return render(request, template_name, {'object':server})