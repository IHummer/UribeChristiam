from django.shortcuts import render
# importamos tablas para generar conteo
from inventory.models import *
from usuarios.models import *
from mascotas.models import *

def index(request):
    productos = Producto.objects.count()
    usuarios = Usuario.objects.count()
    mascotas = Mascota.objects.count()
    context = {
        'header' : 'Inicio',
        'productos': productos,
        'usuarios': usuarios,
        'mascotas': mascotas
    }
    return render(request, 'index.html', context)