# Res Framework
from rest_framework import permissions

class isOwner(permissions.BasePermission):
    '''
    En esta clase lo que haremos será comprobar que 
    solamente el usuario que haya creado dicho objeto,
    pueda modificarlo y/o eliminarlo.

    Si no es el dueño de dicho objeto, no tendrá los
    permisos para ello, y por tanto sólo podrán acceder
    a los métodos de lectura...
    '''
    message = 'No es el propietario'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            '''
            En este if preguntamos si la petición está dentro
            de los métodos 'seguros' como son el GET, OPTIONS,
            HEAD... Oséase, los que no permiten escritura...
            '''
        return request.user == obj.owner