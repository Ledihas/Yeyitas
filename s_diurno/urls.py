# s_diurno/urls.py
from django.urls import path
from . import views # Usa .views para importar las vistas

# Eliminar static de aquí
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 's_diurno' # ¡CORREGIDO! Antes era 'ofert_dia_list'.
                      # Es vital que 'app_name' coincida con lo que el include espera
                      # (generalmente el nombre de la app, 's_diurno').

urlpatterns = [
   path('ofertasD/', views.ofrt_dia_list, name='ofertasD'), # -> s_diurno:ofertasD
   path('desayuno/', views.desa_list, name='desayuno'), # -> s_diurno:desayuno
   path('dia/', views.dia_list, name='dia'), # -> s_diurno:dia
]
# if settings.DEBUG: # Eliminar esto de aquí
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)