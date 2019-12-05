from django.db import models
from usuarios.models import *
from inventory.models import *
import os

class Mascota(models.Model):
    nomb_mascota = models.CharField(max_length=200)
    tip_mascota = models.ForeignKey(Tipomascota, on_delete=models.CASCADE)
    opciones_genero = (
        ('MACHO', 'Macho'),
        ('HEMBRA', 'Hembra')
    )
    genero_mascota = models.CharField(max_length=10, choices=opciones_genero, default="MACHO")
    raza_mascota = models.CharField(max_length=60, blank=True, null=True)
    propietario_mascota = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomb_mascota

