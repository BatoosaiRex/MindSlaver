from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartas/', include('cartas.urls')),
    path('', include('cartas.urls')), # Conecta la raíz directamente a la vista
]# mi_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cartas.urls')),  # Aquí conecta las rutas de la app
]