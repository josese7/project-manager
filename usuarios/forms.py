from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
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
                  'roles',
                  'password'
                  )
        widgets = {
            'password': forms.PasswordInput(),
            'roles': forms.CheckboxSelectMultiple(),
        }
    def save(self, commit=True):
        """
        Metodo para guardar el formulario 

        :user.set_password: encripta la contraseña como django lo necesita
        :param commit: indicador de guardado en la base de datos, True: se debe guardar,
                                                                  False: No guardar.
        :return: El objeto creado por el formulario luego de ejecutar el metodo en el formulario
        """
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            self.save_m2m()
        return user

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
                  'descripcion',
                  'roles'
                  )
        widgets = {
            'password': forms.PasswordInput(),
            'roles': forms.CheckboxSelectMultiple(),
        }
    

    
