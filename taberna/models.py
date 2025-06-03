from djongo import models

class OfrtTab(models.Model):
   # _id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
   

    def __str__(self):
        return self.nombre

class Bebidas(OfrtTab):

    def __str__(self):
        return self.nombre
    
class Specials(OfrtTab):
    beneficio = models.TextField()

    def __str__(self):
        return self.nombre


