from django.shortcuts import render
#añadiendo las tablas
from .models import Categoria, Producto
# Create your views here.
def index(request):
    return render(request, 'inventario/index.html')
