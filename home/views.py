from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventory.models import *

# Create your views here.
# @login_required(redirect_field_name='')
def index(request):
    productos = Producto.objects.count()
    context = {
        'header' : 'Inicio',
        'productos': productos,
    }
    return render(request, 'index.html', context)
# @login_required(redirect_field_name='')
# def inventario(request):
#     return render(request, 'inventario/index.html')