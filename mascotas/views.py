from django.shortcuts import render, redirect, get_object_or_404
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
        item_mascota = Mascota.objects.get(pk=item_id)
        item_detalle = DetalleMascota.objects.filter(mascota=item_id)
        item_registro = RegistroClinico.objects.filter(mascota=item_id)
        mascota = get_object_or_404(Mascota, pk=item_id)
        form_det_masc = FormDetalleMascota(request.POST or None)
        form_reg = FormRegistroClinico(request.POST or None)

        if form_det_masc.is_valid():
            nform_det_masc = form_det_masc.save(commit=False) # Don't save it yet
            nform_det_masc.mascota = mascota # Add person
            nform_det_masc.save() # Now save it
            return redirect('mascotas:perfil_mascota', item_id=item_id)
        elif form_reg.is_valid():
            nform_reg = form_reg.save(commit=False) # Don't save it yet
            nform_reg.mascota = mascota # Add person
            nform_reg.save() # Now save it
            return redirect('mascotas:perfil_mascota', item_id=item_id)
        
        
        context = {
        'item_mascota' : item_mascota,
        'header' : 'Detalles de Mascota: ',
        'item_detalle': item_detalle,
        'item_registro': item_registro,
        'form_det_masc': form_det_masc,
        'form_reg' : form_reg
        }
    except Mascota.DoesNotExist:
        raise Http404("Mascota no existe")
    return render(request, 'mascotas/perfil.html', context)

def editar_detalle(request, item_id):
    item = DetalleMascota.objects.get(pk=item_id)
    if request.method == "POST":
        form = FormDetalleMascota(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('mascotas:perfil_mascota', item_id=item_id)
    else:
        form = FormDetalleMascota(instance=item)
        context = {
            'tipo_titulo': 'tipo_titulo',
            'tipo_boton' : 'tipo_boton',
            'form' : form,
        }
        return render(request, 'mascotas/editar_detalle.html', context)



