from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.views.generic.base import TemplateView

from Gestion_Inst.models import Ciclo
from .forms import *



#------------------------------------------------------------------------------
#esta funcion filtra los pacientes ya sea por documento, nombre y apellido
#se pueden convinar
def selectorCiclos(request):
	#pregunto si el metodo de envio de datos es POST(si se envian datos, si no devuelvo un formulario de busqueda vacio)
	if request.method == "POST":
	#obtengo los valos de los inputTExt del formulario
	    q = request.POST['descripcion']

	    ciclos = []

	    #convino los filtros de busqueda teniendo en cuenta los campos que lleno el usuario en el fomrulario
	    if not q:
	    	ciclos = ciclos = Ciclo.objects.all()#Ciclo.objects.filter(nombres__icontains=q)
        #else:
        #    ciclos = Ciclo.objects.all()
	    #creo un nuevo formulario
	    form = buscadorCicloForm()
	    #pregunto si hubo resultado en la busqueda, si no devulvo el formulario para realizar otra consulta
	    if len(ciclos) != 0:
	    	return render(request, 'Gestion_Inst/Selectores/selectorCiclos.html', {'ciclos':ciclos, 'form':form})
	    else:
	    	return render(request, 'Gestion_Inst/Selectores/selectorCiclos.html', {'form':form})

	else:
		form = buscadorCicloForm()
		return render(request, 'Gestion_Inst/Selectores/selectorCiclos.html', {'form':form})