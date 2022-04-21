from django import forms
from .models import Proyecto
from django.forms.widgets import SelectDateWidget

""" class DateInput(forms.DateInput):
    input_type = 'date' """
class ProyectoForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Proyecto
    """
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)
        #Change date field's widget here
        self.fields['fecha_inicio'].widget = SelectDateWidget()
        self.fields['fecha_fin'].widget = SelectDateWidget()

    def clean(self):
        cleaned_data = super(ProyectoForm, self).clean()
        fecha_ini = cleaned_data.get('fecha_inicio')
        fecha_fin= cleaned_data.get('fecha_fin')
        if fecha_ini.strftime('%y-%m-%d') > fecha_fin.strftime('%y-%m-%d'):
          raise forms.ValidationError('La fecha de inicio del proyecto no puede ser mayor que la fecha final del mismo')
        return cleaned_data


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
        labels= {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'fecha_inicio': 'Fecha de Inicio (dd-mm-yyyy)',
            'fecha_fin': 'Fecha de finalizacion (dd-mm-yyyy)',
        }


        widgets = {
            
        }