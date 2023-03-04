from django.shortcuts import render
from .models import Project #necesitamos hacer referencia a nuestro modelo Project para recuperar sus instancias y enviarlas al template

# Create your views here.

def portfolio(request):
    projects = Project.objects.all() #recuperar los registros de la tabla Projects
    return render(request, 'portfolio/portfolio.html',  {'projects':projects}) #inyectar al template