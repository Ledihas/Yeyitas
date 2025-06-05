# accounts/views.py (asumo que es este archivo)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy # Importado pero no usado directamente en estas vistas
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm
from .models import Reservation
from evento.models import Evento

# --- Vista de Registro ---
def register_view(request):
    # Lógica: Si el usuario ya está autenticado, no tiene sentido que se registre de nuevo.
    # Redirección: Lo enviamos a la lista principal de eventos.
    if request.user.is_authenticated:
        messages.info(request, "Ya estás autenticado.")
        return redirect('evento:eventos') # Redirige a la lista de eventos de la app 'evento'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            pwd = form.cleaned_data['password']
            new_user.set_password(pwd)
            new_user.save()

            messages.success(request, "Registro exitoso. Ya puedes iniciar sesión.")
            # Lógica: Tras un registro exitoso, llevar al usuario a la página de login para que inicie sesión.
            # Redirección: 'accounts:login' es el patrón de login dentro del namespace 'accounts'.
            return redirect('accounts:login')
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else: # GET request
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# --- Vista de Inicio de Sesión ---
def login_view(request): # NOTA: Tenías dos definiciones de login_view, asegúrate de tener solo una.
    # Lógica: Si el usuario ya está autenticado, no debe ver la página de login.
    # Redirección: Lo enviamos a la lista principal de eventos.
    if request.user.is_authenticated:
        messages.info(request, "Ya estás autenticado.")
        return redirect('evento:eventos')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, f"¡Bienvenido, {user.username}!")
            # Lógica: Tras un login exitoso, dirigir al usuario a la página deseada.
            # 'evento:eventos' es una buena elección como página de bienvenida.
            # También podrías usar `settings.LOGIN_REDIRECT_URL` si lo tienes configurado.
            return redirect('evento:eventos')
        else:
            messages.error(request, "Credenciales inválidas.")
    else: # GET request
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# --- Vista de Cerrar Sesión ---
@login_required
def logout_view(request):
    # Lógica: Cerrar la sesión del usuario.
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    # Lógica: Tras cerrar sesión, redirigir a una página pública.
    # Redirección: 'ofertas:ofertas' es el patrón que tienes definido para tu lista de ofertas.
    # Si quieres redirigir al login o a la home, usarías:
    # return redirect('accounts:login') # Redirige a la página de login
    # return redirect('home') # Redirige a la página de inicio del sitio
    return redirect('ofertas:ofertas')

# --- Vista para Hacer una Reserva ---
@login_required
def make_reservation(request, event_id): # NOTA: Tenías dos definiciones de make_reservation, asegúrate de tener solo una.
    """
    Vista para que el usuario haga una reserva a un evento.
    """
    user = request.user
    try:
        event = Evento.objects.get(pk=event_id)
    except Evento.DoesNotExist:
        messages.error(request, "El evento no existe.")
        # Lógica: Si el evento no existe, redirigir a la lista de eventos.
        # Redirección: 'evento:eventos' es el patrón para la lista de eventos.
        return redirect('evento:eventos')

    # Lógica: Evitar reservas duplicadas.
    existing = Reservation.objects.filter(user=user, event=event).exists()
    if existing:
        messages.error(request, "Ya tienes una reserva para este evento.")
        # Lógica: Si ya reservó, redirigir a la página de detalles de ese evento.
        # Redirección: 'evento:detalle_evento' es el patrón para los detalles del evento.
        # Le pasamos el 'pk' del evento.
        return redirect('evento:detalle_evento', pk=event.pk) # ¡Corregido en urls.py de evento!

    # Lógica: Crear la reserva.
    Reservation.objects.create(user=user, event=event)
    # Lógica: Mensaje de confirmación. Asumo que el modelo Evento tiene un campo 'nombre'.
    messages.success(request, f"Reserva confirmada para el evento: {event.nombre if hasattr(event, 'nombre') else event.title}")
    # Lógica: Después de reservar, llevar al usuario a su lista de reservas.
    # Redirección: 'accounts:user_reservations' es el patrón para las reservas del usuario.
    return redirect('accounts:user_reservations')

# --- Vista para Mostrar Reservas del Usuario ---
@login_required
def user_reservations(request):
    """
    Muestra las reservas del usuario.
    """
    reservas = Reservation.objects.filter(user=request.user).select_related('event')
    return render(request, 'accounts/user_reservations.html', {'reservas': reservas})