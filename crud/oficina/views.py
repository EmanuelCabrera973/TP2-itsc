from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Oficina
from .forms import OficinaForm

def lista_oficinas(request):
    oficinas_list = Oficina.objects.all().order_by('nombre')
    paginator = Paginator(oficinas_list, 10)  # 10 oficinas por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'oficinas/lista_oficinas.html', {'page_obj': page_obj})

def detalle_oficina(request, id):
    oficina = get_object_or_404(Oficina, id=id)
    personas = oficina.persona_set.all()  # Todas las personas de esta oficina
    return render(request, 'oficinas/detalle_oficina.html', {
        'oficina': oficina,
        'personas': personas
    })

@login_required
def nueva_oficina(request):
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_oficinas')
    else:
        form = OficinaForm()
    
    return render(request, 'oficinas/nueva_oficina.html', {'form': form})

@login_required
def editar_oficina(request, id):
    oficina = get_object_or_404(Oficina, id=id)
    
    if request.method == 'POST':
        form = OficinaForm(request.POST, instance=oficina)
        if form.is_valid():
            form.save()
            return redirect('detalle_oficina', id=oficina.id)
    else:
        form = OficinaForm(instance=oficina)
    
    return render(request, 'oficinas/editar_oficina.html', {'form': form, 'oficina': oficina})

@login_required
def eliminar_oficina(request, id):
    oficina = get_object_or_404(Oficina, id=id)
    
    if request.method == 'POST':
        oficina.delete()
        return redirect('lista_oficinas')
    
    return render(request, 'oficinas/eliminar_oficina.html', {'oficina': oficina})

def buscar_oficinas(request):
    query = request.GET.get('q', '')
    if query:
        oficinas = Oficina.objects.filter(nombre__icontains=query)
    else:
        oficinas = Oficina.objects.all()
    
    paginator = Paginator(oficinas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'oficinas/buscar_oficinas.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required
def carga_masiva_oficinas(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo = request.FILES['archivo']
        # Implementar lógica de carga masiva aquí
        # Por ahora solo un mensaje
        return render(request, 'oficinas/carga_masiva_oficinas.html', {
            'mensaje': 'Carga masiva implementada parcialmente'
        })
    
    return render(request, 'oficinas/carga_masiva_oficinas.html')

