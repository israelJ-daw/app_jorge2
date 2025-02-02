from django.urls import path

from .api_views import *

urlpatterns = [
    
    path('usuarios/', usuario_lista2),
    path('propiedades/', propiedad_lista2, name='propiedad_lista2'),
    path('categorias/', categoria_lista2, name='categoria_lista2'),
]