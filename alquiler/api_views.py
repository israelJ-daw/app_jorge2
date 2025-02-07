from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Count, Q
from .forms import *
from rest_framework import status


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


@api_view(['GET'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def usuarios_busqueda_simple(request):
    formulario = BusquedaUsuarioForm(request.GET)  # Usar request.GET en @api_view
    
    if formulario.is_valid():
        texto = formulario.cleaned_data.get('textoBusqueda')

        # Filtrar los usuarios con el texto de búsqueda
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=texto) | Q(email__icontains=texto)
        )

        # Serializar los usuarios y devolverlos
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    else:
        return Response(formulario.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes([AllowAny])
def usuarios_busqueda_avanzada_api(request):
    usuarios = Usuario.objects.all()  # Comenzamos con todos los usuarios
    formulario = BusquedaAvanzadaUsuarioForm(request.GET)

    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        email = formulario.cleaned_data.get('email')
        telefono = formulario.cleaned_data.get('telefono')
        fecha_registro_desde = formulario.cleaned_data.get('fecha_registro_desde')
        fecha_registro_hasta = formulario.cleaned_data.get('fecha_registro_hasta')

        if nombre:
            usuarios = usuarios.filter(nombre__icontains=nombre)
        if email:
            usuarios = usuarios.filter(email__icontains=email)
        if telefono:
            usuarios = usuarios.filter(telefono__icontains=telefono)
        if fecha_registro_desde:
            usuarios = usuarios.filter(fecha_registro__gte=fecha_registro_desde)
        if fecha_registro_hasta:
            usuarios = usuarios.filter(fecha_registro__lte=fecha_registro_hasta)

    # Serializamos los usuarios para enviarlos como respuesta JSON
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def categoria_busqueda_avanzada_api(request):
    categorias = Categoria.objects.all()
    formulario = BusquedaCategoriaForm(request.GET)

    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        premiun = formulario.cleaned_data.get('premiun')
        principal = formulario.cleaned_data.get('principal')

        if nombre:
            categorias = categorias.filter(nombre__icontains=nombre)
        if premiun is not None:
            categorias = categorias.filter(premiun=premiun)
        if principal is not None:
            categorias = categorias.filter(principal=principal)

    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def propiedad_busqueda_avanzada_api(request):
    propiedades = Propiedad.objects.all()
    formulario = BusquedaPropiedadForm(request.GET)

    if formulario.is_valid():
        titulo = formulario.cleaned_data.get('titulo')
        precio_min = formulario.cleaned_data.get('precio_min')
        max_usuarios = formulario.cleaned_data.get('max_usuarios')

        if titulo:
            propiedades = propiedades.filter(titulo__icontains=titulo)
        if precio_min is not None:
            propiedades = propiedades.filter(precio_por_noche__gte=precio_min)
        if max_usuarios is not None:
            propiedades = propiedades.filter(max_usuarios__gte=max_usuarios)

    serializer = PropiedadSerializer(propiedades, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def servicio_extra_busqueda_avanzada_api(request):
    servicios_extra = ServicioExtra.objects.all()
    formulario = BusquedaServicioExtraForm(request.GET)

    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        precio_max = formulario.cleaned_data.get('precio_max')
        disponible = formulario.cleaned_data.get('disponible')

        if nombre:
            servicios_extra = servicios_extra.filter(nombre__icontains=nombre)
        if precio_max is not None:
            servicios_extra = servicios_extra.filter(precio__lte=precio_max)
        if disponible is not None:
            servicios_extra = servicios_extra.filter(disponible=disponible)

    serializer = ServicioExtraSerializer(servicios_extra, many=True)
    return Response(serializer.data)
