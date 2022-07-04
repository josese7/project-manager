from django.db import models
from usuarios.models import *

from datetime import datetime, timedelta
import calendar

PENDIENTE = 0
ENCURSO = 1
FINALIZADO = 2
ESTADOS_PROYECTO = (
    (PENDIENTE, 'Pendiente'),
    (ENCURSO, 'En curso'),
    (FINALIZADO,'Finalizado')
)
class Proyecto(models.Model):
    nombre= models.CharField( max_length=50, null= False, blank=False, default=' ')
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio= models.DateField(blank=False, null=False, default=datetime.now())
    fecha_fin= models.DateField(blank=False, null=False, default=datetime.now() + timedelta(days=60))
    usuarios= models.ManyToManyField('usuarios.Usuario', blank=False)
    estado = models.PositiveIntegerField(default=PENDIENTE, choices=ESTADOS_PROYECTO) 
    

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre
    def get_usuarios(self):
        print(self.request)
