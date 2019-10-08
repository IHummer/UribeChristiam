from django.shortcuts import render
from .models import Usuario
# Create your views here.

def index(request):
    return render(request, 'usuarios/index.html')
