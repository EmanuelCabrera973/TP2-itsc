from django.db import models
from oficina.models import Oficina

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    