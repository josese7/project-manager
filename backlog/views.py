from django.shortcuts import render
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


from usuarios.models import Usuario
from proyecto.models import Proyecto
from backlog.models import Backlog, UserStory, Comentario
# Create your views here.
@method_decorator(login_required, name='dispatch')
class ListBacklogView(ListView):
    model= Backlog
    template_name= 'backlogs/list_backlogs.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context
    


@method_decorator(login_required, name='dispatch')
class UpdateBacklogView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'proyectos/update_proyecto.html'
    model = Backlog
    success_url = '/project/'
    form_class = BacklogForm
    success_message = 'Se ha modificado el proyecto'

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context

@method_decorator(login_required, name='dispatch')
class DetailBacklogView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Backlog
    template_name = 'backlogs/detail_backlog2.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        backlog= Backlog.objects.get(pk=self.kwargs['pk'])
        context["us"] = backlog.userstory_set.all()


        return context


""" USER STORIES"""
@method_decorator(login_required, name='dispatch')
class CreateUserStoryView( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'userstories/create_userstory.html'
    model = UserStory
    success_url = '/desarrollo'
    form_class = UserStoryForm
    success_message = 'Se ha creado el User Story'

    def get_form_kwargs(self):
        kwargs = super(CreateUserStoryView, self).get_form_kwargs()
        
        backlog = Backlog.objects.filter(pk=self.kwargs['pk']).first()
       
        print(self.kwargs['pk'])

        kwargs['backlog'] =backlog # pasamos el backlog a los kwargs del formulario
        return kwargs

    def get_success_url(self):
        
        return reverse('detail_backlog', kwargs={'pk': self.object.backlog.pk})
    
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        print(self.kwargs) 
        backlog= Backlog.objects.get(pk=self.kwargs['pk']) 
     

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        context["backlog"] = backlog
       


        return context
    def form_valid(self, form):
        
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class DetailUserStoryView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = UserStory
    template_name = 'userstories/detail_userstory.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()

        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
    
        return context

@method_decorator(login_required, name='dispatch')
class UpdateUserStoryView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'userstories/update_userstory.html'
    model = UserStory
    success_url = '/desarrollo/'
    form_class = UserStoryUpdateForm
    success_message = 'Se ha modificado el UserStory'

    def get_form_kwargs(self):
        kwargs = super(UpdateUserStoryView, self).get_form_kwargs()
        
        us = UserStory.objects.filter(pk=self.kwargs['pk']).first()
       
        print(self.kwargs['pk'])

        kwargs['backlog'] =us.backlog # pasamos el backlog a los kwargs del formulario
        return kwargs

    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       
       


        return context



@method_decorator(login_required, name='dispatch')
class DeleteUserStoryView( LoginRequiredMixin, DeleteView):
    model= UserStory
    success_url= '/desarrollo/'
    template_name= 'userstories/delete_userstory.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context


""" Comentario """
@method_decorator(login_required, name='dispatch')
class ListComentarioView(ListView):
    model= Comentario
    template_name= 'backlogs/list_comentario_us.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context
@method_decorator(login_required, name='dispatch')
class CreateComentarioUs( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'userstories/create_comentario_us.html'
    model = Comentario
    form_class = ComentarioUSForm
    success_message = 'Se ha creado el Comentario'
    
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
    
        return context
    def post(self, request, *args, **kwargs):
        """
        Metodo que es ejecutado al darse una consulta POST
        :param request: consulta recibida
        :param args: argumentos adicionales
        :param kwargs: diccionario de datos adicionales
        :return: la respuesta a la consulta POST
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        self.object 
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())