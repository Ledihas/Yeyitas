from django.db import connection, models
import psycopg2
#from traitlets import This

class Evento(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
    
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
    
class ReservaManager(models.Manager):
        def eliminar(self, a_nombre):
            
            try:
                conn = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="zaza",
                password="1234"
                )
                cursor = conn.cursor()
                cursor.execute(f""" 
                            DELETE FROM public.evento_reserva WHERE a_nombre = %s
                            """,(a_nombre,))
                conn.commit()
                #print(cursor.fetchone())
                return f"Eliminados: {cursor.rowcount}"

            
            except Exception as error:
                return {f"Error: {error}"}
    
class Reserva(models.Model):
    nombre_evento = models.CharField(max_length=100)
    a_nombre = models.CharField(max_length=100)
    
    objects = ReservaManager()
    

    
    
    #def get_nombre():
        
    #    return This.a_nombre
    
    def __str__(self):
        return self.a_nombre
    