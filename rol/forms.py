from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Rol
        fields = ('nombre',
                  'descripcion',
                  'permisos',
                  )
    
