from django.urls import path
from . import views

app_name = 'mascotas'
urlpatterns = [
    path('', views.index, name='index'),
    path('nueva_mascota/', views.nueva_mascota, name='nueva_mascota'),
    path('<int:item_id>/', views.perfil_mascota, name='perfil_mascota')
]