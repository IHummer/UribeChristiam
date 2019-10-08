from django.db import models

# Create your models here.

class Usuario(models.Model):
    nomb_usurio = models.CharField(max_length=200)

    


    