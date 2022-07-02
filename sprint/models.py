from django.db import models
from backlog.models import *
from proyecto.models import *
"""
Definicion de los estados de Sprint
"""
PENDIENTE = 0
ENCURSO = 1
FINALIZADO = 2
ESTADOS_SPRINT = (
    (PENDIENTE, 'Pendiente'),
    (ENCURSO, 'En curso'),
    (FINALIZADO,'Finalizado')
)
# Create your models here.
class Sprint(models.Model):
    nombre = models.CharField( max_length=50, null= False, blank=False, default=' ')
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_fin = models.DateField(blank=False, null=False)
    proyecto = models.ForeignKey(
        'proyecto.Proyecto',
        on_delete=models.CASCADE,
    )
    estado = models.PositiveIntegerField(default=PENDIENTE, choices=ESTADOS_SPRINT) 

    def __str__(self):
        """
        Retorna el nombre del permiso actual
        :return: retorna el valor del campo nombre del objeto actual
        """
        return self.nombre

    def get_user_stories(self):
        """
        metodo del modelo Sprint que retorna todos los user stories asignados al sprint
        :return: Todos los user stories del sprint
        """
        return UserStory.objects.filter(sprint=self.pk)