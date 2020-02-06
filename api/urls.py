# Django
from django.urls import path

# Routers
from rest_framework.routers import DefaultRouter

# Rest Framework
from rest_framework.authtoken import views

# Json Web Token
from rest_framework_simplejwt import views as jwt_views

# Documentation
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='RestFul Api Curso DRF Udemy')

# CoreAPI
from rest_framework.documentation import include_docs_urls


# API Views
from .apiviews import ProductoList, ProductoDetalle

# from .apiviews import CategoriaSave, SubCategoriaSave
from .apiviews import CategoriaList, SubCategoriaList,\
    CategoriaDetalle,\
    SubCategoriaAdd,\
    ProductoViewSet

from .apiviews import UserCreate
from .apiviews import LoginView


router = DefaultRouter() #Instancia
router.register('v2/productos', ProductoViewSet, basename='productos')


urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),

    path('v1/categorias/', CategoriaList.as_view(), name='categoria_save'),
    # path('v1/subcategorias/', SubCategoriaList.as_view(), name='subcategoria_save'),
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='sc_list'),
    
    #SubCategoriaAdd
    path('v1/categorias/<int:cat_pk>/add_subcategoria/', SubCategoriaAdd.as_view(), name='sc_add'),

    # Autenticación de Usuarios
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_creado'),

    path('v4/login/', LoginView.as_view(), name='login'),

    # Otra forma de obtener un token para login, usando una vista genérica de Rest Framework
    path('v4/login-drf/', views.obtain_auth_token, name='login-drf'),

    # Swagger Docs
    path('swagger-docs/', schema_view),

    # CoreApi
    path('coreapi-docs/', include_docs_urls(title='Documentación COREAPI')),

    # JWT
    path('v5/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('v5/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]

urlpatterns += router.urls