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
from Gestion_Inst.models import Curso



class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ('descripcion',)

    def __init__(self,*args,**kwargs):
        super(CursoForm,self).__init__(*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )

def curso_list(request, template_name='Gestion_Inst/Curso/curso_list.html'):
    servers = Curso.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)

def curso_create(request, template_name='Gestion_Inst/Curso/curso_form.html'):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request, template_name, {'form':form})

def curso_update(request, pk, template_name='Gestion_Inst/Curso/curso_form.html'):
    server = get_object_or_404(Nivel, pk=pk)
    form = CursoForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('curso_list')
    return render(request, template_name, {'form':form})

def curso_delete(request, pk, template_name='Gestion_Inst/Curso/curso_confirm_delete.html'):
    server = get_object_or_404(Nivel, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('curso_list')
    return render(request, template_name, {'object':server})