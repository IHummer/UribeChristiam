from django.db import models

# Create your models here.
class Categoria(models.Model):
    cat_nomb = models.CharField(max_length=150, blank=False)
    def __str__(self):
        return self.cat_nomb

class Producto(models.Model):
    prod_nomb = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    opciones_estado = (
        ('DISPONIBLE', 'Listo para ser vendido'),
        ('AGOTADO', 'Producto agotado'),
        ('REABASTECIENDO', 'Reabastecimiento en proceso')
    )
    estado = models.CharField(max_length=20, choices=opciones_estado, default="DISPONIBLE")
    cat_prod = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return 'Nombre: {0} Precio: {1}'.format(self.prod_nomb, self.precio)
