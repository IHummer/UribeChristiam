from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

def index(request):
    items = Mascota.objects.all()
    context = {
        'items_mascota' : items,
        'header' : 'Mascotas Registrados',
    }
    return render(request, 'mascotas/index.html', context)
    
# Apartado independiente de crear nueva mascota
# def nueva_mascota(request):
#     if request.method ==  "POST":
#         form = FormMascota(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('mascotas:index')
#     else:
#         form = FormMascota()
#         return render(request, 'mascotas/nueva_mascota.html', {'form': form})

# vista para cada mascota
def perfil_mascota(request, item_id):
    try:
        item = Mascota.objects.get(pk=item_id)
        context = {
        'item' : item,
        'header' : 'Detalles de Mascota: ',
        }
    except Mascota.DoesNotExist:
        raise Http404("Mascota no existe")
    return render(request, 'mascotas/perfil.html', context)
