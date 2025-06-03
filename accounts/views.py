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
        return redirect('home')
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
        return redirect('home')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Credenciales inválidas.")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect('home')

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
