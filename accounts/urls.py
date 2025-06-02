from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('reservations/', views.user_reservations, name='user_reservations'),
    path('reservar/<int:event_id>/', views.make_reservation, name='make_reservation'),
]
