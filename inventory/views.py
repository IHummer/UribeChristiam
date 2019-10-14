from django.shortcuts import render, redirect
#añadiendo las tablas
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

# @login_required(redirect_field_name='')
def index(request):
    items = Producto.objects.all()
    context = {
        'items_prod' : items,
        'header' : 'Inventario',
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
