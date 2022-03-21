
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic.base import TemplateView

@method_decorator(login_required, name='dispatch')
class SecurityView(TemplateView):

    template_name = 'modulos/seguridad.html'
    def get(self, request, *args, **kwargs):

        permisos = request.user.get_permisos()
        return self.render_to_response(self.get_context_data(permisos=permisos))

    def get_context_data(self, **kwargs):
        context = super(SecurityView, self).get_context_data(**kwargs)

        return context
