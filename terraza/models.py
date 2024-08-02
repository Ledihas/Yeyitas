from django.db import models

class OfrtTerraza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='ofertasTer/', null=True, blank=True)


    def __str__(self):
        return self.nombre
    
class Helados(OfrtTerraza):
  
    def __str__(self):
        return self.nombre
    

class Bebidas(OfrtTerraza):
<<<<<<< HEAD
    alcohol = models.DecimalField(max_digits=8, decimal_places=2,max_length=100)
=======
    alcohol = models.DecimalField(max_digits=5, decimal_places=3)
>>>>>>> e26df79 (Descripción de los cambios realizados)

    def __str__(self):
        return self.nombre
    
class Platos(OfrtTerraza):

    def __str__(self):
        return self.nombre
    