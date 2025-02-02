from .models import * 
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import *


@api_view(['GET'])
def usuario_lista2(request):
    
    usuarios= Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)