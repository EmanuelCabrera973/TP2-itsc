from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'edad', 'oficina']  # Campos a mostrar
    list_filter = ['oficina', 'edad']  # Filtros laterales  
    search_fields = ['apellido', 'nombre']  # Campos buscables
    ordering = ['apellido', 'nombre']  # Ordenamiento por defecto