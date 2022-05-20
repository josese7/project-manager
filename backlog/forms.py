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
        fields = ('nombre',)

class UserStoryForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    def __init__(self, backlog, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        #Change date field's widget here
        print(backlog)
        b = self.fields['backlog'].widget
        backlogs = []
        backlogs.append((backlog.pk, backlog.nombre))
        b.choices = backlogs
       

    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = UserStory
        fields = ('nombre', 'descripcion', 'backlog')

       

    