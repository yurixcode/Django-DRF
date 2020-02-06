# Django
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Models
from .models import Categoria


def categoria_list(request):
    MAX_OBJECTS = 20
    cat = Categoria.objects.all()[:MAX_OBJECTS]

    data = {'results': list(cat.values('descripcion', 'activo'))}
    return JsonResponse(data)

def categoria_detalle(request, pk):
    cat = get_object_or_404(Categoria, pk=pk)
    data = {
        'results' : {
            'descripcion': cat.descripcion,
            'activo': cat.activo
        }
    }
    
    return JsonResponse(data)


# Categoria.objects.bulk_create([
#     Categoria(descripcion='Desarrollo Web con Django', activo=False),
#     Categoria(descripcion='Replicación con SymmetricsDS', activo=True),
#     Categoria(descripcion='Dominando ORM de Django', activo=True),
#     Categoria(descripcion='Restful Api con Django Framework ', activo=False),
#     Categoria(descripcion='Administración PostgreSQL', activo=True)
# ])