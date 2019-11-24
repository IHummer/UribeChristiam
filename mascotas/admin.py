from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(RazaMascota, Mascota)
class ViewAdmin(admin.ModelAdmin):
    pass