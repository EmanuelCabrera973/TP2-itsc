from django import forms
from .models import Oficina

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = ['nombre', 'nombre_corto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_corto': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre completo',
            'nombre_corto': 'Nombre corto',
        }