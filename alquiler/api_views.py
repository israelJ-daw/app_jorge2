from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def usuario_lista2(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)
