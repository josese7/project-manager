from django.db import models



"""
Declaracion de variables para la seleccion de tipo de permiso
"""
tipoSistema = '1'
tipoProyecto = '2'

tipos_permiso = [
    (tipoSistema, 'Permiso de sistema'),
    (tipoProyecto, 'Permiso de proyecto')
]
"""
Definicion de los modelos de Permiso y Rol
"""

class Permiso(models.Model):
    """
    Datos para el modelo  permisos
    """
    nombre = models.CharField(max_length=70, blank=False, null=False)
    """
    tipo 1 = Permisos de administracion
    tipo 2 = Permisos de Proyecto
    """

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre


class Rol(models.Model):
    """
    Datos para el modelo Rol
    """
    nombre = models.CharField(max_length=50, unique=True, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    permisos = models.ManyToManyField('Permiso', blank=False)

    def __str__(self):
        """
        Retorna el nombre del rol actual
        :return: retorna el valor del campo nombre del objeto
        """
        return self.nombre