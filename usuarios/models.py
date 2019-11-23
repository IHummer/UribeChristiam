from django.db import models
from phone_field import PhoneField

# las tablas

class Usuario(models.Model):
    nomb_usr = models.CharField(max_length=200)
    ap_usr = models.CharField(max_length=200)
    tel_usr = PhoneField(blank=True, help_text='Teléfono de contacto')
    cel_usr = PhoneField(blank=False, help_text='Celular de contacto')
    dir_usr = models.CharField(max_length=300)
    def __str__(self):
        return self.nomb_usr


    


    