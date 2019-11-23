from django.shortcuts import render, redirect
#añadiendo las tablas
from .models import *

from .forms import *
# Create your views here.

def index(request):
    items = Producto.objects.all()
    context = {
        'items_prod' : items,
        'header' : 'Inventario de productos',
    }
    return render(request, 'inventario/index.html', context)

def nuevoProd(request):
    
    if request.method ==  "POST":
        form = FormProducto(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventario:index')
    else:
        form = FormProducto()
        return render(request, 'inventario/nuevo_prod.html', {'form': form})

def nuevoCatMarMasc(request, cls):
    if request.method ==  "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario:nuevo_prod')
    else:
        form = cls()
        return render(request, 'inventario/nuevo_prod_1.html', {'form': form})

def nuevoCat(request):
    return nuevoCatMarMasc(request, FormCategoria)

def nuevoMar(request):
    return nuevoCatMarMasc(request, FormMarca)

def nuevoMasc(request):
    return nuevoCatMarMasc(request, FormTipomascota)
