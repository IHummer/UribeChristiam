from django import forms
from .models import *
from django.utils.translation import ugettext_lazy as _

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('prod_nomb', 'precio', 'estado', 'cat_prod')
        widgets = {
            'prod_nomb': forms.TextInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'precio': forms.NumberInput(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'estado': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    }),
            'cat_prod': forms.Select(
                attrs={
                    'oninvalid': 'this.setCustomValidity("Por favor llene el campo")',
                    'oninput': 'setCustomValidity("")'
                    })
            }
        labels = {
            'prod_nomb': _('Nombre del producto'),
            'precio': _('Precio en soles'),
            'estado': _('Estado del producto'),
            'cat_prod': _('Categoría del producto'),
        }