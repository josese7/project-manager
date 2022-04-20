from django.shortcuts import render
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


from usuarios.models import Usuario
from proyecto.models import Proyecto
# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProyectoListView(ListView):
    model= Proyecto
    template_name= 'proyectos/list_proyecto.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context

@method_decorator(login_required, name='dispatch')
class DetailProyectoView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Proyecto
    template_name = 'proyectos/detail_proyecto.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context
    
@method_decorator(login_required, name='dispatch')
class CreateProyectoView( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'proyectos/create_proyecto.html'
    model = Proyecto
    success_url = '/proyectos/'
    form_class = ProyectoForm
    success_message = 'Se ha creado el proyecto'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context


@method_decorator(login_required, name='dispatch')
class UpdateProyectoView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'proyectos/update_proyecto.html'
    model = Proyecto
    success_url = '/proyectos/'
    form_class = ProyectoForm
    success_message = 'Se ha modificado el proyecto'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context

@method_decorator(login_required, name='dispatch')
class DeleteProyectoView( LoginRequiredMixin, DeleteView):
    model= Proyecto
    success_url= '/proyectos/'
    template_name= 'proyectos/delete_proyecto.html'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context