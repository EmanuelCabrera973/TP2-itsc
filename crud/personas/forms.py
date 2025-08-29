from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['apellido', 'nombre', 'edad', 'oficina']
        widgets = {
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'oficina': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'apellido': 'Apellido',
            'nombre': 'Nombre',
            'edad': 'Edad',
            'oficina': 'Oficina',
        }