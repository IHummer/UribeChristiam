from django.urls import path
from . import views

app_name = 'inventario'
urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo_prod/', views.nuevoProd, name='nuevo_prod'),
]