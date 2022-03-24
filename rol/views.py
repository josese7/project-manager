from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from rol.models import Rol
from .forms import *


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListRolView(ListView):
    model= Rol
    template_name= 'roles/list_rol.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context


@method_decorator(login_required, name='dispatch')
class DetailRolView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Rol
    template_name = 'roles/detail_rol.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context

@method_decorator(login_required, name='dispatch')
class RolListView2(LoginRequiredMixin, ListView):
    """
    Clase de la vista de la lista de Roles
    """
    template_name = 'roles/list_rol.html'
    queryset = Rol.objects.all()
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context


@method_decorator(login_required, name='dispatch')
class CreateRolView( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'roles/create_rol.html'
    model = Rol
    success_url = '/security/roles/'
    form_class = RolForm
    success_message = 'Se ha creado el rol'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context

@method_decorator(login_required, name='dispatch')
class UpdateRolView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'roles/update_rol.html'
    model = Rol
    success_url = '/security/roles/'
    form_class = RolForm
    success_message = 'Se ha modificado el Rol'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context

@method_decorator(login_required, name='dispatch')
class DeleteRolView( LoginRequiredMixin, DeleteView):
    model= Rol
    success_url= '/security/roles/'
    template_name= 'roles/delete_rol.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context
