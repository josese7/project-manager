from django.db import models
from proyecto.models import *
"""
Definicion de los estados de User Story
"""
PENDIENTE = 2
ASIGNADO = 1
FINALIZADO = 0
ESTADOS_US = (
    (PENDIENTE, 'Pendiente'),
    (ASIGNADO, 'Asignado'),
    (FINALIZADO,'Finalizado')
)
class UserStory(models.Model):
    nombre= models.CharField( max_length=50, null= False, blank=False, default=' ')
    descripcion = models.TextField(blank=True, null=True)
    backlog = models.ForeignKey(
        'Backlog',
        on_delete=models.CASCADE,
    )
    usuarios =  models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL, null = True, default=None
    )
    
    estado = models.PositiveIntegerField(default=PENDIENTE, choices=ESTADOS_US) 

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

class Comentario(models.Model):
    usuario = models.CharField( max_length=50, null= False, blank=False, default=' ')
    descripcion = models.TextField(blank=False, null=False)
    estado = models.CharField( max_length=50, null= False, blank=False, default=' ') 
    fecha = models.DateField(blank=False, null=False, default=datetime.now())
    userstory = models.ForeignKey(
        'UserStory',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.descripcion
