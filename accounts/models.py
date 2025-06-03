from djongo import models
from django.conf import settings

# Importa tu modelo de Evento; ajusta el path si tu app tiene otro nombre
from evento.models import Evento  

class Reservation(models.Model):
    #_id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Evento, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
