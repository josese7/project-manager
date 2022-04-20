from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Proyecto
        fields = ('nombre',
                  'descripcion',
                  'fecha_inicio',
                  'fecha_fin'
                  )