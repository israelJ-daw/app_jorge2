from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Count


@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def usuario_lista2(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def propiedad_lista2(request):
    precio_max = request.GET.get('precio_max', None)  
    if precio_max:
        propiedades = Propiedad.objects.filter(precio_por_noche__lte=precio_max).order_by('precio_por_noche')
    else:
        propiedades = Propiedad.objects.all().order_by('precio_por_noche')
    
    serializer = PropiedadSerializer(propiedades, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def categoria_lista2(request):
    categorias = Categoria.objects.annotate(num_propiedades=Count('propiedades')) 
    
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)
