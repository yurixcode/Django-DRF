from django.db import models

from django.conf import settings

class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract=True


class Categoria(OwnerModel):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria',
        unique=True

    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Categorias'


class SubCategoria(OwnerModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Sub Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    class Meta:
        verbose_name_plural = 'Sub Categorías'
        unique_together = ('categoria', 'descripcion')


class Producto(OwnerModel):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Productos'



# Producto.objects.bulk_create([
#     Producto(subcategoria_id=1, descripcion='Frontend', fecha_creado='2019-10-01T12:11:37.090335Z'),
#     Producto(subcategoria_id=2, descripcion='Backend', fecha_creado='2019-10-01T12:11:37.090335Z'),
#     Producto(subcategoria_id=3, descripcion='DevOps', fecha_creado='2019-10-01T12:11:37.090335Z'),
#     Producto(subcategoria_id=4, descripcion='Marketing', fecha_creado='2019-10-01T12:11:37.090335Z'),
#     Producto(subcategoria_id=5, descripcion='Ventas', fecha_creado='2019-10-01T12:11:37.090335Z')
# ])