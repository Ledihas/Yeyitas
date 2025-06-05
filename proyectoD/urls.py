# proyectoD/urls.py - ¡VERSiÓN CORREGIDA FINAL!
from django.contrib import admin
from django.urls import path, include
from hola import views as hola_views
from accounts import views as accounts_views # Necesaria si tu logout o otras vistas están aquí
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. Página de inicio del sitio
    path('', hola_views.Home, name='home'), # ¡Crucial para redirigir a 'home'!

    # 2. URLs de autenticación y cuentas (tu app 'accounts')
    # Usamos 'namespace="accounts"' para que las redirecciones como 'accounts:login' funcionen.
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # 3. Inclusiones de URLs de tus aplicaciones (¡Una sola vez por prefijo de URL!)
    # Asumimos que cada app_name en sus respectivos urls.py coincide con el nombre de la app o el namespace deseado.
    path('s_diurno/', include('s_diurno.urls')),
    path('ofertas/', include('hola.urls')), # La app 'hola' tiene app_name='ofertas'
    path('terraza/', include('terraza.urls')),
    path('taberna/', include('taberna.urls')),
    path('evento/', include('evento.urls')),

    # 4. Vistas directas de 'hola' que no están bajo un prefijo de URL
    # Es buena práctica nombrarlas para poder redirigir a ellas.
    path('nosotros/', hola_views.nosotros, name='nosotros'),
    path('contacto/', hola_views.contacto, name='contacto'),
    path('jefeLog/', hola_views.vista_login, name='jefe_login'),
    path('adminSite/', hola_views.login_supUser, name='admin_site_login'),

    # 5. La URL de logout
    # Si 'logout_view' está en tu app 'accounts', usa el namespace 'accounts'.
    # Si quieres usar la de Django, se incluye en 'accounts.urls' por defecto sin namespace.
    # Si es tu vista `logout` de `hola.views` (como está actualmente), usa su nombre si está definida.
    # Dado que tienes `accounts_views.logout_view` en tu app 'accounts', ¡úsa esa!
    path('logout/', accounts_views.logout_view, name='logout'), # Apunta a tu vista de logout en 'accounts'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)