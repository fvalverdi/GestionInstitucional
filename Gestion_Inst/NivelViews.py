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
from Gestion_Inst.models import Alumno, Nivel



class NivelEnsenanzaForm(forms.ModelForm):

    class Meta:
        model = Nivel
        fields = ('descripcion',)

    def __init__(self,*args,**kwargs):
        super(NivelEnsenanzaForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def nivel_list(request, template_name='Gestion_Inst/Nivel/nivel_list.html'):
    servers = Nivel.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def nivel_create(request, template_name='Gestion_Inst/Nivel/nivel_form.html'):
    form = NivelEnsenanzaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nivel_list')
    return render(request, template_name, {'form':form})

def nivel_update(request, pk, template_name='Gestion_Inst/Nivel/nivel_form.html'):
    server = get_object_or_404(Nivel, pk=pk)
    form = NivelEnsenanzaForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('nivel_list')
    return render(request, template_name, {'form':form})

def nivel_delete(request, pk, template_name='Gestion_Inst/Nivel/nivel_confirm_delete.html'):
    server = get_object_or_404(Nivel, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('nivel_list')
    return render(request, template_name, {'object':server})

def nivel_borrar(request, pk):
    server = get_object_or_404(Nivel, pk=pk)

    server.delete()
    return redirect('nivel_list')
