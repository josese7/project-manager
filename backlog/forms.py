from django import forms
from .models import Backlog, UserStory

class BacklogForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Backlog
        fields = ('nombre')
        
