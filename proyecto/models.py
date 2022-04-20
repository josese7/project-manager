from django.db import models
from usuarios.models import *
pendiente = '1'
enCurso= '2'
terminado='3'

tipos_permiso = [
    (pendiente, 'Pendiente'),
    (enCurso, 'En curso'),
    (terminado, 'Terminado')
]
class Proyecto(models.Model):
    nombre: models.CharField( max_length=50, null= False, blank=False)
    descripcion: models.CharField( max_length=50)
    fecha_inicio: models.DateField(blank=True, null=True)
    fecha_fin: models.DateField(blank=True, null=True)
    usuarios: models.ManyToManyField('usuario.Usuario', blank=False)

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre
