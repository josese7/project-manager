from django import forms
from .models import Sprint
from django.forms.widgets import SelectDateWidget
from datetime import datetime, timedelta


""" class DateInput(forms.DateInput):
    input_type = 'date' """
class SprintForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Proyecto
    """

    def __init__(self, proyecto, *args, **kwargs):
        super(SprintForm, self).__init__(*args, **kwargs)
        #Change date field's widget hereWS
        self.fields['fecha_inicio'].widget = SelectDateWidget()
        
        sprints= Sprint.objects.filter(proyecto_id=proyecto.pk)
        cant_sprint = sprints.count()
        print('Sprint cant')
        print(cant_sprint)

        if(cant_sprint > 0):
            last_sprint = sprints.last()
            self.fields['fecha_inicio'].initial = last_sprint.fecha_fin
        else:
            self.fields['fecha_inicio'].initial = proyecto.fecha_inicio
        
        self.fields['fecha_fin'].widget = forms.HiddenInput()
        self.fields['fecha_fin'].initial = self.fields['fecha_inicio'].initial + timedelta(days=15)
            
            


        
        b = self.fields['proyecto'].widget
        
        proyectos = []
        proyectos.append((proyecto.pk, proyecto.nombre))
        b.choices = proyectos



    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Sprint
        fields = ('nombre',
                  'fecha_inicio',
                  'fecha_fin',
                  'estado',
                  'proyecto'
                  )


        widgets = {
            
        }


class SprintUpdateForm(forms.ModelForm):
    """
    Formulario para la creacion de un  Usuario
    """

    class Meta:
        """
        Clase en la que se definen los datos necesarios y adicionales para inicializacion y
        visualizacion del formulario
        """
        model = Sprint
        fields = ('nombre', 'fecha_inicio','fecha_fin', 'estado')