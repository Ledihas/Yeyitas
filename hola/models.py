from django.db import models
<<<<<<< HEAD


=======
from django.contrib import auth

class Admin_log(models.Model):
    nombre = models.CharField(max_length=100)
    username = models.CharField(max_length= 100, primary_key= True)
    contraseña = models.TextField(max_length=50)
    is_autentiqued = models.BooleanField()

    def __str__(self):
        return self.nombre
>>>>>>> e26df79 (Descripción de los cambios realizados)
