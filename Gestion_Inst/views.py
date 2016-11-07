from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
# Create your views here.
from django.template.context_processors import csrf

from Gestion_Inst.forms import AlumnoForm,NivelEnsenanzaForm
from Gestion_Inst.models import *

def index(request):
    return render(request, 'Gestion_Inst/index.html', {})

#crear Alumno
def crearAlumno(request):
    if request.POST:
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = AlumnoForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Gestion_Inst/Alumno/crear_alumno.html', args)

def crearNivelEnsenanza(request):
    if request.POST:
        form = NivelEnsenanzaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        form = NivelEnsenanzaForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Gestion_Inst/Nivel/crear_nivel.html', args)


def editarNivelEnsenanza(request,pk):
    if request.POST:
        form = NivelEnsenanzaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')
    else:
        nivel = Nivel.objects.get(pk=pk)
        form = NivelEnsenanzaForm(nivel)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('Gestion_Inst/Nivel/crear_nivel.html', args)