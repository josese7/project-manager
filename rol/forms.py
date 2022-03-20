from django import forms
from .models import Rol, Permiso

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
        widgets = {
            'permisos': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        """
        Constructor del formulario
        :param args: argumentos para inicializacion
        :param kwargs: diccionario de datos adicionales para inicializacion
        """
        super(RolForm, self).__init__(*args, **kwargs)
        permisos_all = Permiso.objects.all()
        p = self.fields['permisos'].widget
        permisos = []
        for permiso in permisos_all:
            permisos.append((permiso.id, permiso.nombre))
        p.choices = permisos
