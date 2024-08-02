from django.db import models

class OfrtTab(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='ofertas/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Bebidas(OfrtTab):
    alcohol = models.DecimalField(max_digits=5,decimal_places=3)
    
    def __str__(self):
        return self.nombre
    
class Specials(OfrtTab):
    beneficio = models.TextField()

    def __str__(self):
        return self.nombre


