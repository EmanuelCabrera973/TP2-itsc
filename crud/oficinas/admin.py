from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Oficina

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nombre_corto']  # Campos a mostrar en la lista
    search_fields = ['nombre', 'nombre_corto']  # Campos buscables
    list_filter = ['nombre']  # Filtros laterales