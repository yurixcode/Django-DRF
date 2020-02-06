# Django Rest Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Auth
from django.contrib.auth.models import User

# Models
from .models import Producto, Categoria, SubCategoria


class ProductoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Producto
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    
    class Meta:
        model=Categoria
        fields='__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    
    class Meta:
        model=SubCategoria
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        # No queremos que devuelva la contraseña en el response, 
        # de modo que haremos lo siguiente:
        extra_kwargs = { 'password': {'write_only': True} }

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        Token.objects.create(user=user)
        
        return user


# prod_serializer = ProductoSerializer(
#     data={
#         "subcategoria":16,
#         "descripcion":"5Daaesarrollo Web con Python usando Django 2.1",
#         "fecha_creado":"2019-10-01T12:11:37.090335Z"
#     })