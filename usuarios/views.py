from django.shortcuts import render, redirect
#añadiendo las tablas
from django.http import HttpResponse, Http404
from .models import *

from .forms import *

def index(request):
    items = Usuario.objects.all()
    context = {
        'items_usr' : items,
        'header' : 'Usuarios Registrados',
    }
    return render(request, 'usuarios/index.html', context)

def nuevo_usr(request):
    if request.method ==  "POST":
        form = FormUsuario(request.POST)

        if form.is_valid():
            form.save()
            return redirect('usuarios:index')
    else:
        form = FormUsuario()
        return render(request, 'usuarios/nuevo_usr.html', {'form': form})

# vista para cada usuario
def perfil_usr(request, item_id):
    try:
        item = Usuario.objects.get(pk=item_id)
        context = {
        'item' : item,
        'header' : 'Perfil de Usuario: ',
        }
        
    except Usuario.DoesNotExist:
        raise Http404("Usuario no existe")
    return render(request, 'usuarios/perfil.html', context)
