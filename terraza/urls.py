# terraza/urls.py
from django.urls import path
from . import views # Usa .views para importar las vistas
# Eliminar static de aquí
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'terraza' # ¡Correcto!

urlpatterns = [
   path('ofertasT/', views.ofert_list, name='ofertasT'), # -> terraza:ofertasT
   path('helados/', views.helados_list, name='helados'), # -> terraza:helados
   path('bebidas/', views.bebidas_list, name='bebidas'), # -> terraza:bebidas
   path('platos/', views.platos_list, name='platos'), # -> terraza:platos
]
# if settings.DEBUG: # Eliminar esto de aquí
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)