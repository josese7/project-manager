
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.base import TemplateView

@method_decorator(login_required, name='dispatch')
class SecurityView(TemplateView):

    template_name = 'modulos/seguridad.html'
    
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context
