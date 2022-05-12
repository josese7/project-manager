from django.db import models
from proyecto.models import *

class UserStory(models.Model):
    nombre= models.CharField( max_length=50, null= False, blank=False, default=' ')
    descripcion = models.TextField(blank=True, null=True)
    backlog = models.ForeignKey(
        'Backlog',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre



class Backlog(models.Model):
    nombre= models.CharField( max_length=50, null= False, blank=False, default=' ')
    proyecto = models.OneToOneField(
        'proyecto.Proyecto',
        on_delete=models.CASCADE,
        null=True
    )
    

    def __str__(self):
        """
        Retorna el nombre del backlog
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre

