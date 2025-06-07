from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template,Context
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from hola.models import Admin_log

def cantidad_reservas():
    reservas = Reserva.objects.all()
    i = 0
    for r in reservas:
        i+=1
    print (i)
    return i 
    



def eventos_list(request):
    eventos = Evento.objects.all()
      
    if request.method == 'POST':
        # Obtener los datos del formulario
        cantidad = request.POST.get('cantidad')
        nombre_evento = request.POST.get('nombre_evento')
        a_nombre = request.POST.get('a_nombre')

        # Validar los datos (puedes agregar más validaciones según sea necesario)
        if cantidad and nombre_evento and a_nombre:
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
        else:
            # Manejar el error si los datos no son válidos
            return HttpResponse("Error: Todos los campos son obligatorios.")

    return render(request, 'eventos_list.html', {'eventos': eventos})

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
    
