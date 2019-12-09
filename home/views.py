from django.shortcuts import render
# importamos tablas para generar conteo
from inventory.models import *
from usuarios.models import *
from mascotas.models import *
from todo.models import Task
from django.db.models import Q
from django.utils import timezone

def index(request):
    productos = Producto.objects.count()
    usuarios = Usuario.objects.count()
    mascotas = Mascota.objects.count()
    # tabla y número de items agotados
    items_agotados = Producto.objects.filter(Q(estado='AGOTADO')|Q(estado='REABASTECIENDO')).order_by('estado')
    num_agotados = Producto.objects.filter(estado='AGOTADO').count()
    # variables para tareas despues de hoy
    hoy = timezone.now()
    tasks_act = Task.objects.filter(completed=False, due_date__gt=hoy).order_by('due_date')
    # primeras 3 tareas
    tasks_primeras = Task.objects.filter()[:3]

    context = {
        'header' : 'Inicio',
        'productos': productos,
        'usuarios': usuarios,
        'mascotas': mascotas,
        'items_agotados' : items_agotados,
        'num_agotados' : num_agotados,
        'tasks_act' : tasks_act,
    }
    return render(request, 'index.html', context)