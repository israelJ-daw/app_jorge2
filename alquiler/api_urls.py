from django.urls import path

from .api_views import *

urlpatterns = [
    
    path('usuarios/', usuario_lista2)
]