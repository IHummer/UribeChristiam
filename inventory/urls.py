from django.urls import path
from . import views

app_name = 'inventario'
urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo_prod/', views.nuevoProd, name='nuevo_prod'),
    # path('nuevo_cat/', views.nuevoCat, name='nuevo_cat'),
    # path('nuevo_marc/', views.nuevoMar, name='nuevo_marc'),
    # path('nuevo_tipmascota/', views.nuevoMasc, name='nuevo_tipmascota'),
]