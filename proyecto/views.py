from django.shortcuts import render
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from backlog.models import Backlog
from usuarios.models import Usuario
from proyecto.models import Proyecto
# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProyectoListView(ListView):
    model= Proyecto
    template_name= 'proyectos/list_proyecto.html'
    def get(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta GET
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta GET
        """
        self.object_list = Proyecto.objects.all()

        backlog= None
        for proyecto in self.object_list:
                try:
                    nombre_bg= "Backlog de "+proyecto.nombre 
                    backlog = Backlog(proyecto=proyecto, nombre=nombre_bg)
                    backlog.save()
                except:
                    print('hola')
           
               

        return self.render_to_response(self.get_context_data(object_list=self.object_list))
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

        proyecto= Proyecto.objects.get(pk=self.kwargs['pk'])
        backlog=Backlog.objects.get(pk=proyecto.pk)
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        context["backlog"] = backlog

        return context
    
@method_decorator(login_required, name='dispatch')
class CreateProyectoView( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'proyectos/create_proyecto.html'
    model = Proyecto
    success_url = '/project/'
    form_class = ProyectoForm
    success_message = 'Se ha creado el proyecto'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()

        print(self.kwargs)
        
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
    success_url = '/project/'
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
    success_url= '/project'
    template_name= 'proyectos/delete_proyecto.html'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context
    

@method_decorator(login_required, name='dispatch')
class ListProyectoUserView( LoginRequiredMixin, TemplateView):

    template_name = 'proyectos/list_proyecto_users.html'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()

        proyecto= Proyecto.objects.get(pk=self.kwargs['pk'])
        usuarios = proyecto.usuarios.all()
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        context["object_list"] = usuarios
        context["view"] = 'Proyecto'
        context["proyecto"] = proyecto
        print(self.kwargs)
        print(proyecto.pk)
 
        return context
        
@method_decorator(login_required, name='dispatch')
class ManageProyectoUserView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'proyectos/update_proyecto.html'
    model = Proyecto
    success_url = '/project/'
    form_class = ProyectoUserForm
    success_message = 'Se ha modificado el proyecto'

    def get_success_url(self):
         return reverse('detail_proyecto', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context