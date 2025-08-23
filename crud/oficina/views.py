from django.shortcuts import render
from .models import Oficina

def lista_oficina(request):
    # Esta función mostraría la lista de oficinas
    oficinas = Oficina.objects.all()
    return render(request, 'oficina/lista_oficinas.html', {'oficinas': oficinas})