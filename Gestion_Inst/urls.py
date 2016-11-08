"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from Gestion_Inst import views, CursoViews, NivelViews, DivisionViews, CategoriaViews, CicloViews, AlumnosViews

urlpatterns = [
    url(r'^$', views.index,name='index'),


    #Alumno
    url(r'^newAlumno/$', AlumnosViews.alumno_create, name='crearAlumno'),
    url(r'^alumnos', AlumnosViews.alumnos_list, name='alumnos_list'),
    url(r'^editarAlumno/(?P<pk>[0-9]+)', AlumnosViews.alumno_update, name='editarAlumno'),
    url(r'^deleteAlumno/(?P<pk>\d+)$', AlumnosViews.alumno_delete, name='alumno_delete'),

    #amb Nivel

    url(r'^niveles$', NivelViews.nivel_list, name='nivel_list'),
    url(r'^newNivel$', NivelViews.nivel_create, name='nivel_new'),
    url(r'^editNivel/(?P<pk>\d+)$', NivelViews.nivel_update, name='nivel_edit'),
    url(r'^deleteNivel/(?P<pk>\d+)$', NivelViews.nivel_delete, name='nivel_delete'),

    #amb Curso

    url(r'^cursos$', CursoViews.curso_list, name='curso_list'),
    url(r'^newCurso$', CursoViews.curso_create, name='curso_new'),
    url(r'^editCurso/(?P<pk>\d+)$', CursoViews.curso_update, name='curso_edit'),
    url(r'^deleteCurso/(?P<pk>\d+)$', CursoViews.curso_delete, name='curso_delete'),

    #amb Division

    url(r'^divisiones', DivisionViews.division_list, name='division_list'),
    url(r'^newDivision$', DivisionViews.division_create, name='division_new'),
    url(r'^editDivision/(?P<pk>\d+)$', DivisionViews.division_update, name='division_edit'),
    url(r'^deleteDivision/(?P<pk>\d+)$', DivisionViews.division_delete, name='division_delete'),

     #amb Categorias

    url(r'^categorias', CategoriaViews.categoria_list, name='categoria_list'),
    url(r'^newCaegoria$', CategoriaViews.categoria_create, name='categoria_new'),
    url(r'^editCategoria/(?P<pk>\d+)$', CategoriaViews.categoria_update, name='categoria_edit'),
    url(r'^deleteCategoria/(?P<pk>\d+)$', CategoriaViews.categoria_delete, name='categoria_delete'),

     #amb Ciclo

    url(r'^ciclos', CicloViews.ciclo_list, name='ciclo_list'),
    url(r'^newCiclo$', CicloViews.ciclo_create, name='ciclo_new'),
    url(r'^editCiclo/(?P<pk>\d+)$', CicloViews.ciclo_update, name='ciclo_edit'),
    url(r'^deleteCiclo/(?P<pk>\d+)$', CicloViews.ciclo_delete, name='ciclo_delete'),

]
