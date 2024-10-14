from django.db import models

class OfrtTerraza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
   

    def __str__(self):
        return self.nombre
    
class Helados(OfrtTerraza):
  
    def __str__(self):
        return self.nombre
    

class Bebidas(OfrtTerraza):
    

    def __str__(self):
        return self.nombre
    
class Platos(OfrtTerraza):

    def __str__(self):
        return self.nombre
    
