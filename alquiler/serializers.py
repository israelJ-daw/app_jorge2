from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  
        fields = ['nombre', 'email']  
        


class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'  

class CategoriaSerializer(serializers.ModelSerializer):
    num_propiedades = serializers.IntegerField() 

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'num_propiedades'] 