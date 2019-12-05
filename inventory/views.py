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
        formproducto = FormProducto(request.POST)
        formcat = FormCategoria(request.POST)
        formmarc = FormMarca(request.POST)
        formmasc = FormTipomascota(request.POST)
        if formproducto.is_valid():
            formproducto.save()
            return redirect('inventario:index')
        elif formcat.is_valid():
            formcat.save()
            return redirect('inventario:nuevo_prod')
        elif formmarc.is_valid():
            formmarc.save()
            return redirect('inventario:nuevo_prod')
        elif formmasc.is_valid():
            formmasc.save()
            return redirect('inventario:nuevo_prod')
    else:
        formproducto = FormProducto()
        formcat = FormCategoria()
        formmarc = FormMarca()
        formmasc = FormTipomascota()
        context = {
            'formproducto' : formproducto,
            'formcat' : formcat,
            'formmarc' : formmarc,
            'formmasc' : formmasc,
        }
        return render(request, 'inventario/nuevo_prod.html', context)





# def nuevoCatMarMasc(request, cls):
#     if request.method ==  "POST":
#         form = cls(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('inventario:nuevo_prod')
#     else:
#         form = cls()
#         return render(request, 'inventario/nuevo_prod_1.html', {'form': form})

# def nuevoCat(request):
#     return nuevoCatMarMasc(request, FormCategoria)

# def nuevoMar(request):
#     return nuevoCatMarMasc(request, FormMarca)

# def nuevoMasc(request):
#     return nuevoCatMarMasc(request, FormTipomascota)
