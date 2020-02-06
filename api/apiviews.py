# Rest Framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Django
#from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth import authenticate

# APIViews
from rest_framework import viewsets

# Models
from .models import Producto, SubCategoria, Categoria

# Serializers
from .serializers import ProductoSerializer
from .serializers import CategoriaSerializer
from .serializers import SubCategoriaSerializer
from .serializers import UserSerializer

# Permissions
from .permissions import isOwner

# RestFramework Permission
from rest_framework.permissions import IsAuthenticated


'''
-Use viewsets.ModelViewSet cuando va a permitir todas 
o la mayoría de las operaciones CRUD en un modelo.

-Use genéricos.* Cuando solo desee permitir algunas 
operaciones en un modelo

-Usa APIView cuando quieras personalizar completamente 
el comportamiento
'''

# class ProductoList(APIView):

#     def get(self, request):
#         prod = Producto.objects.all()[:20] #queryset
#         data = ProductoSerializer(prod, many=True).data
#         return Response(data)


# class ProductoDetalle(APIView):
#     def get(self, request, pk):
#         prod = get_object_or_404(Producto, pk=pk)
#         data = ProductoSerializer(prod).data
#         return Response(data)


class ProductoList(generics.ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaSave(generics.CreateAPIView):
    serializer_class = CategoriaSerializer

class SubCategoriaSave(generics.CreateAPIView):
    serializer_class = SubCategoriaSerializer


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# class SubCategoriaList(generics.ListCreateAPIView):
#     queryset = SubCategoria.objects.all()
#     serializer_class = SubCategoriaSerializer


class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class SubCategoriaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs['pk'])
        return queryset

    serializer_class = SubCategoriaSerializer


class SubCategoriaAdd(APIView):
    '''
    Aquí permitimos solamente peticiones POST
    '''
    def post(self, request, cat_pk):
        descripcion = request.data.get('descripcion') #Obtenemos el campo que se envía
        data = {'categoria': cat_pk, 'descripcion': descripcion}

        serializer = SubCategoriaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoViewSet(viewsets.ModelViewSet):
    '''
    Permite el CRUD completo.

    Al usar ViewSet no es necesario diseñar las URL nosotros mismos, 
    se puede hacer automáticamente.
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = ([IsAuthenticated, isOwner])


# Autentificación
class UserCreate(generics.CreateAPIView):
    '''
    Vista para crear un nuevo usuario.
    '''
    # En la vista UserCreate, debemos anular la configuración global de autenticación
    # para esto debemos setear en vacío las propiedades authentication_classes y permission_classes,
    # agregándole lo siguiente a la clase UserCreate
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

class LoginView(APIView):
    '''
    Esta sería la forma 'manual' de crear la vista, también podemos
    utilizar una vista génerica que nos ofrece DRF. Llamada 'obtain_auth_token', la tenemos importada en las URLs de esta aplicación.
    '''
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Credenciales Incorrectas', 'otra info':'Pos esta es la otra info'}, status=status.HTTP_400_BAD_REQUEST)