from django.db import models

class OfrtDia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
    


    def __str__(self):
        return self.nombre

class OfrtDesa(OfrtDia):
   
    def __str__(self):
        return self.nombre
