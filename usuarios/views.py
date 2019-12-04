from django.shortcuts import render, redirect, get_object_or_404
#añadiendo las tablas
from django.http import HttpResponse, Http404
from .models import *
from mascotas.forms import *
from mascotas.models import *
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
        items = Mascota.objects.filter(propietario_mascota=item_id)
        propietario_mascota = get_object_or_404(Usuario, pk=item_id)
        form = FormMascota(request.POST or None)
        item = Usuario.objects.get(pk=item_id)
        if form.is_valid():
            nform = form.save(commit=False) # Don't save it yet
            nform.propietario_mascota = propietario_mascota # Add person
            nform.save() # Now save it
            return redirect('usuarios:perfil_usr', item_id=item_id)
        context = {
        'item' : item,
        'header' : 'Perfil de Usuario: ',
        'form' : form,
        'items_mascota' : items,
        }
    except Usuario.DoesNotExist:
        raise Http404("Usuario no existe")
    return render(request, 'usuarios/perfil.html', context)

# CREAR NUEVA MASCOTA PARA USUARIO EN APARTADO
# def nueva_mascota_perfil_usr(request, item_id):
#     propietario_mascota = get_object_or_404(Usuario, pk=item_id)
#     form = FormMascota(request.POST or None)
#     if form.is_valid():
#         nform = form.save(commit=False) # Don't save it yet
#         nform.propietario_mascota = propietario_mascota # Add person
#         nform.save() # Now save it
#         return redirect('mascotas:index')
#     return render(request, 'mascotas/nueva_mascota_2.html', {'form': form})