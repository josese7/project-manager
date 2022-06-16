from django import forms
from .models import Backlog, UserStory
from usuarios.models import Usuario

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
        fields = ('nombre', 'descripcion', 'usuarios')


class ComentarUSForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """ 
    def __init__(self, backlog, *args, **kwargs):
        super(ComentarUSForm, self).__init__(*args, **kwargs)
        #Change date field's widget hereWS
        c = self.fields['comentario'].widget

    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = UserStory
        fields = ('comentario',)
        widget = forms.TextInput(attrs={'placeholder': 'Type name here...'})

       

    