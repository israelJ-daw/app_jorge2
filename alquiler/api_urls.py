from django.urls import path
from .api_views import *

urlpatterns = [
    path('usuarios/', usuario_lista2),
    path('propiedades/', propiedad_lista2, name='propiedad_lista2'),
    path('categorias/', categoria_lista2, name='categoria_lista2'),
    path('usuarios/busqueda_simple/', usuarios_busqueda_simple, name='usuarios_busqueda_simple'),
    path('usuarios/busqueda_avanzada/', usuarios_busqueda_avanzada_api, name='usuarios_busqueda_avanzada_api'),
    path('categorias/busqueda_avanzada/', categoria_busqueda_avanzada_api, name='categoria_busqueda_avanzada_api'),
    path('propiedades/busqueda_avanzada/', propiedad_busqueda_avanzada_api, name='propiedad_busqueda_avanzada_api'),
    path('servicios_extra/busqueda_avanzada/', servicio_extra_busqueda_avanzada_api, name='servicio_extra_busqueda_avanzada_api'),

]
