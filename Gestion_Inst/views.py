from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Gestion_Inst/index.html', {})