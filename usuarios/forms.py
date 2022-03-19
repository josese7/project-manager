from django import forms
from .models import Usuario

class CreateUserForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Usuario
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'estado',
                  'ci',
                  'telefono',
                  'direccion',
                  'descripcion',
                  'password'
                  )
        widgets = {
            'password': forms.PasswordInput()
        }

class UpdateUserForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """
    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Usuario
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'estado',
                  'ci',
                  'telefono',
                  'direccion',
                  'descripcion'
                  )

    
