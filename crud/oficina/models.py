from django.db import models

# Create your models here.
class Oficina(models.Model):
    nombre = models.CharField(max_Length=100)
    nombre_corto = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
    
