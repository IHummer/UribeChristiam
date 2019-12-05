from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class FormMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nomb_mascota', 'tip_mascota', 'genero_mascota', 'raza_mascota',)
        widgets = {
            'nomb_mascota': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'tip_mascota': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'genero_mascota': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'raza_mascota': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'nomb_mascota': _('Nombre de la mascota'),
            'tip_mascota': _('Especie de la mascota'),
            'genero_mascota': _('Elegir Género'),
            'raza_mascota': _('Raza')
        }