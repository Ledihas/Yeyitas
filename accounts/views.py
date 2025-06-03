from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm
from .models import Reservation
from evento.models import Evento

def register_view(request):
    if request.user.is_authenticated:
        return redirect('evento:eventos')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            pwd = form.cleaned_data['password']
            new_user.set_password(pwd)
            new_user.save()
            messages.success(request, "Registro exitoso. Ya puedes iniciar sesión.")
            return redirect('login')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('evento:eventos')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect('evento:eventos')
        else:
            messages.error(request, "Credenciales inválidas.")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('ofertas:ofertas')

@login_required
def make_reservation(request, event_id):
    """
    Vista para que el usuario haga una reserva a un evento.
    """
    user = request.user
    try:
        event = Evento.objects.get(pk=event_id)
    except Evento.DoesNotExist:
        messages.error(request, "El evento no existe.")
        return redirect('event_list')
    
    # Verificar si ya existe reserva
    existing = Reservation.objects.filter(user=user, event=event).exists()
    if existing:
        messages.error(request, "Ya tienes una reserva para este evento.")
        return redirect('event_detail', event_id=event.id)

    # Crear reserva
    Reservation.objects.create(user=user, event=event)
    messages.success(request, f"Reserva confirmada para el evento: {event.title}")
    return redirect('user_reservations')

@login_required
def user_reservations(request):
    """
    Muestra las reservas del usuario.
    """
    reservas = Reservation.objects.filter(user=request.user).select_related('event')
    return render(request, 'accounts/user_reservations.html', {'reservas': reservas})

def login_view(request):
    # Lógica: Si el usuario ya está autenticado, redirigir a la página de eventos.
    if request.user.is_authenticated:
        return redirect('evento:eventos')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() # Obtiene el usuario autenticado
            login(request, user) # Establece la sesión del usuario

            messages.success(request, f"¡Bienvenido, {user.username}!")
            # Lógica: Redirigir después de un login exitoso.
            # Si tienes LOGIN_REDIRECT_URL en settings.py, podrías usarlo.
            # Si quieres una redirección específica, esta es correcta.
            return redirect('evento:eventos')
        else:
            messages.error(request, "Credenciales inválidas.") # Mensaje genérico por seguridad
    else: # Si el método es GET, mostrar un formulario vacío
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def make_reservation(request, event_id):
    """
    Vista para que el usuario haga una reserva a un evento.
    """
    user = request.user
    try:
        # Lógica: Obtener el evento por su ID.
        # Corrección: El nombre del campo ID en Evento.
        # Si estás usando djongo y no definiste _id explícitamente, Django usa 'id'.
        event = Evento.objects.get(pk=event_id)
    except Evento.DoesNotExist:
        messages.error(request, "El evento no existe.")
        # Lógica: Redirigir si el evento no existe.
        # Corrección: 'event_list' debe ser un nombre de patrón de URL existente.
        # Es mejor usar el namespace si lo tienes, por ejemplo:
        return redirect('evento:eventos') # O a la lista de eventos principal

    # Lógica: Verificar si el usuario ya tiene una reserva para este evento.
    existing = Reservation.objects.filter(user=user, event=event).exists()
    if existing:
        messages.error(request, "Ya tienes una reserva para este evento.")
        # Lógica: Redirigir a los detalles del evento si ya reservó.
        # Corrección: 'event_detail' debe ser un nombre de patrón de URL existente.
        # Asegúrate de que el nombre del parámetro URL sea 'pk' si eso espera tu URLconf.
        return redirect('evento:detalle_evento', pk=event.id) # Suponiendo 'detalle_evento' para detalles del evento

    # Lógica: Crear la reserva si no existe.
    Reservation.objects.create(user=user, event=event)
    messages.success(request, f"Reserva confirmada para el evento: {event.nombre}") # Usar event.nombre si es el campo correcto
    # Lógica: Redirigir a las reservas del usuario después de confirmar.
    # Corrección: 'user_reservations' debe ser un nombre de patrón de URL existente.
    return redirect('accounts:user_reservations') # Suponiendo que tus URLs de cuentas tienen namespace 'accounts'


@login_required
def user_reservations(request):
    """
    Muestra las reservas del usuario.
    """
    # Lógica: Obtener todas las reservas del usuario actual.
    # `select_related('event')` es una buena práctica para optimizar consultas
    # si 'event' es un ForeignKey y necesitas acceder a sus campos en la plantilla.
    reservas = Reservation.objects.filter(user=request.user).select_related('event')
    return render(request, 'accounts/user_reservations.html', {'reservas': reservas})