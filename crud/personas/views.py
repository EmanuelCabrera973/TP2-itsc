from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Persona
from .forms import PersonaForm
import csv
from django.contrib import messages
from oficinas.models import Oficina

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

def buscar_persona(request):
    query = request.GET.get('q', '')
    if query:
        personas = Persona.objects.filter(nombre__icontains=query) | Persona.objects.filter(apellido__icontains=query)
    else:
        personas = Persona.objects.all()
    
    paginator = Paginator(personas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'personas/buscar_persona.html', {
        'page_obj': page_obj,
        'query': query
    })



@login_required
def carga_masiva_persona(request):
    if request.method == 'POST' and request.FILES['archivo']:
        archivo = request.FILES['archivo']
        
        try:
            decoded_file = archivo.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            personas_creadas = 0
            errores = []
            
            for row_num, row in enumerate(reader, start=2):
                try:
                    apellido = row['apellido'].strip()
                    nombre = row['nombre'].strip()
                    edad = int(row['edad'])
                    oficina_id = int(row['oficina_id'])
                    
                    # Validaciones
                    if not apellido or not nombre:
                        errores.append(f"Línea {row_num}: Nombre o apellido vacíos")
                        continue
                    
                    if edad < 1 or edad > 120:
                        errores.append(f"Línea {row_num}: Edad inválida")
                        continue
                    
                    # Verificar que la oficina existe
                    try:
                        oficina = Oficina.objects.get(id=oficina_id)
                    except Oficina.DoesNotExist:
                        errores.append(f"Línea {row_num}: Oficina con ID {oficina_id} no existe")
                        continue
                    
                    # Crear la persona
                    Persona.objects.create(
                        apellido=apellido,
                        nombre=nombre,
                        edad=edad,
                        oficina=oficina
                    )
                    personas_creadas += 1
                    
                except (KeyError, ValueError) as e:
                    errores.append(f"Línea {row_num}: Error en datos - {str(e)}")
                except Exception as e:
                    errores.append(f"Línea {row_num}: {str(e)}")
            
            # Mostrar resultados
            if errores:
                messages.warning(request, f'Se crearon {personas_creadas} personas, pero hubo {len(errores)} errores.')
            else:
                messages.success(request, f'¡Éxito! Se crearon {personas_creadas} personas.')
                
            return redirect('lista_personas')
            
        except Exception as e:
            messages.error(request, f'Error al procesar el archivo: {str(e)}')
            return redirect('carga_masiva_persona')
    
    return render(request, 'personas/carga_masiva_persona.html')