from django.views.generic import ListView, CreateView, UpdateView, DetailView
""" from rol.forms import * """
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from rol.models import Rol


@method_decorator(login_required, name='dispatch')
class RolListView(LoginRequiredMixin, ListView):
    """
    Clase de la vista de la lista de Roles
    """
    template_name = 'rol/list_rol.html'
    model = Rol
    queryset = Rol.objects.all()
