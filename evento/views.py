<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib import messages

=======
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template,Context
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from hola.models import Admin_log
>>>>>>> e26df79 (Descripción de los cambios realizados)

def cantidad_reservas():
    reservas = Reserva.objects.all()
    i = 0
    for r in reservas:
        i+=1
    print (i)
    return i 
    

<<<<<<< HEAD
=======


>>>>>>> e26df79 (Descripción de los cambios realizados)
def eventos_list(request):
    eventos = Evento.objects.all()
      
    if request.method == 'POST':
        # Obtener los datos del formulario
        cantidad = request.POST.get('cantidad')
        nombre_evento = request.POST.get('nombre_evento')
        a_nombre = request.POST.get('a_nombre')

        # Validar los datos (puedes agregar más validaciones según sea necesario)
        if cantidad and nombre_evento and a_nombre:
<<<<<<< HEAD
            if cantidad_reservas() > 4 or cantidad_reservas() == 4:
                return HttpResponse("""  <html><body><h1>Aviso:</h1><h3> Las Reservas estan llenas <h/3></body></html> """)
            else:
                R = Reserva()
                R.cantidad = cantidad
                R.nombre_evento = nombre_evento
                R.a_nombre = a_nombre
                R.save()
                # Redirigir a una página de éxito o mostrar un mensaje
                
                return HttpResponse(""" <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>Éxito</title> <style> body { font-family: Arial, sans-serif; background-color: #f0f8ff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; } .success-container { background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.1); text-align: center; } .success-icon { font-size: 80px; color: #4CAF50; margin-bottom: 20px; } .success-message { font-size: 24px; margin-bottom: 30px; } .btn { background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; text-decoration: none; } .btn:hover { background-color: #45a049; } </style> </head> <body> <div class="success-container"> <div class="success-icon">✓</div> <div class="success-message">¡Reserva Realizada!</div> <a href="/" class="btn">Volver al Inicio</a> </div> </body> </html> """)
                # Puedes cambiar esto por una redirección a otra vista

=======
            if cantidad_reservas() > 8 or cantidad_reservas() == 8:
                return HttpResponse("""  <html><body><h1>Aviso:</h1><h3> Las Reservas estan llenas <h/3></body></html> """)
            else:
                try:
                    lol = Reserva.objects.get(a_nombre = a_nombre)
                except :
                    lol = None
                
                if lol == None:
                    
                    R = Reserva()
                    R.cantidad = cantidad
                    R.nombre_evento = nombre_evento
                    R.a_nombre = a_nombre
                    R.save()
                    # Redirigir a una página de éxito o mostrar un mensaje
                    extio = open('hola/templates/exito.html')
                    plt=Template(extio.read())
                    extio.close()
                    ctc= Context()
                    documento = plt.render(ctc)
                    return render(request, 'eventos_list.html', {'ofertas': eventos,'exito':documento})
                    # Puedes cambiar esto por una redirección a otra vista
                else:
                    return render(request, 'eventos_list.html', {'exito': 'Ya existe reservacion a ene nombre'})
>>>>>>> e26df79 (Descripción de los cambios realizados)
        else:
            # Manejar el error si los datos no son válidos
            return HttpResponse("Error: Todos los campos son obligatorios.")

    return render(request, 'eventos_list.html', {'ofertas': eventos})

<<<<<<< HEAD
=======
extio = open('hola/templates/exito.html')

def delete_res(request):
    if request.method == 'POST':
        a = request.POST.get('a_nombre')
        if a :
            try:
                r = Reserva.objects.eliminar(a)
            except:
                print(r)
                return HttpResponse('Error')
            print(a)
            print(r)
            return render(request, 'delete_res.html', {'exito':r})
    elif request.method == 'GET':
        return render(request, 'delete_res.html')
    else: 
        return HttpResponse("Error: Todos los campos son obligatorios.")
    
    


def show_reservas(request):
    if request.session['nombre'] :
        res = Reserva.objects.all()
        return render(request,'reservas.html', {'ofertas': res})
    else:
        return HttpResponseRedirect('/evento/eventos')
    
>>>>>>> e26df79 (Descripción de los cambios realizados)
