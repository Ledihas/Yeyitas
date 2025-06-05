# hola/urls.py
from django.urls import path
from .views import hola_mundo, Home, ofertas, a_nombre, exito
# Eliminar static de aquí
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'ofertas' # ¡Correcto!

urlpatterns = [
    path('hi/', hola_mundo, name='hi'), # Añadido nombre para poder referenciarla
    path('Home/', Home, name='home_hola'), # Le doy un nombre distinto para evitar conflicto con la raíz
    path('ofertas/', ofertas, name='ofertas'), # -> ofertas:ofertas
    path('a_nombre/', a_nombre, name='a_nombre'), # -> ofertas:a_nombre
    path('exito/', exito, name='exito'), # -> ofertas:exito
]
# if settings.DEBUG: # Eliminar esto de aquí
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)