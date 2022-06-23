from django import forms
from .models import Backlog, UserStory, Comentario
from usuarios.models import Usuario
"""
Definicion de los estados de User Story
"""

ESTADOS_US = ['Finalizado', 'Asignado','Pendiente']

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
        #Change date field's widget hereWS
        b = self.fields['backlog'].widget
        
        backlogs = []
        backlogs.append((backlog.pk, backlog.nombre))
        b.choices = backlogs

        u = self.fields['usuarios'].widget
        usuarios = []
        users = backlog.proyecto.usuarios.all()

        for i in users:
            usuarios.append((i.pk, i.username))
        
        u.choices = usuarios

       
       

    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = UserStory
        fields = ('nombre', 'descripcion', 'backlog', 'usuarios')

class UserStoryUpdateForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    def __init__(self, backlog, *args, **kwargs):
        super(UserStoryUpdateForm, self).__init__(*args, **kwargs)

        u = self.fields['usuarios'].widget
        usuarios = []
        users = backlog.proyecto.usuarios.all()

        for i in users:
            usuarios.append((i.pk, i.username))
        
        u.choices = usuarios
        print(backlog)
     
       
       

    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = UserStory
        fields = ('nombre', 'descripcion','usuarios')


class ComentarioUSForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """ 
    def __init__(self, us, *args, **kwargs):
        super(ComentarioUSForm, self).__init__(*args, **kwargs)
      
       #Set userstory field

        us_field = self.fields['userstory'].widget
        userStory=[]
        userStory.append((us.pk, us.nombre))
        us_field.choices = userStory

       
        #Set user field and estado field
        self.fields['usuario'].initial= us.usuarios
        self.fields['estado'].initial= ESTADOS_US[us.estado]
        

    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Comentario
        fields = ('usuario', 'descripcion', 'estado', 'userstory')
        widget = {
            'usuario': forms.HiddenInput()
        }
        

       

    