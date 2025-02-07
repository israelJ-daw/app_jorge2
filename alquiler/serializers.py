from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  
        fields = '__all__'        


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'  

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'premiun', 'principal']

class ServicioExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioExtra
        fields = '__all__'