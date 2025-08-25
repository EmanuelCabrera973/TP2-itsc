from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Persona
from .forms import PersonaForm

def lista_personas(request):
    personas_list = Persona.objects.all().order_by('apellido', 'nombre')
    paginator = Paginator(personas_list, 10)  # 10 personas por página
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'personas/lista_personas.html', {'page_obj': page_obj})

def detalle_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    return render(request, 'personas/detalle_persona.html', {'persona': persona})

@login_required
def nueva_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    
    return render(request, 'personas/nueva_persona.html', {'form': form})

@login_required
def editar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('detalle_persona', id=persona.id)
    else:
        form = PersonaForm(instance=persona)
    
    return render(request, 'personas/editar_persona.html', {'form': form, 'persona': persona})

@login_required
def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, id=id)
    
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    
    return render(request, 'personas/eliminar_persona.html', {'persona': persona})

def buscar_personas(request):
    query = request.GET.get('q', '')
    if query:
        personas = Persona.objects.filter(nombre__icontains=query) | Persona.objects.filter(apellido__icontains=query)
    else:
        personas = Persona.objects.all()
    
    paginator = Paginator(personas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'personas/buscar_personas.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required
def carga_masiva_personas(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo = request.FILES['archivo']
        # Implementar lógica de carga masiva aquí
        return render(request, 'personas/carga_masiva_personas.html', {
            'mensaje': 'Carga masiva implementada parcialmente'
        })
    
    return render(request, 'personas/carga_masiva_personas.html')