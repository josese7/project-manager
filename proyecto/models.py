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
    fecha_inicio: models.DateField(_(""), auto_now=False, auto_now_add=False)
    fecha_fin: models.DateField(_(""), auto_now=False, auto_now_add=False)
    usuarios: models.ManyToManyField("usuarios.Usuario", verbose_name=_(""))
    

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre
