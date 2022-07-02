from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from .forms import *
from usuarios.models import Usuario
from proyecto.models import Proyecto
from backlog.models import Backlog, UserStory
from sprint.models import Sprint
# Create your views here.





@method_decorator(login_required, name='dispatch')
class ListSprintView(ListView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Proyecto
    template_name = 'sprints/list_sprints.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        proyecto= Proyecto.objects.get(pk=self.kwargs['pk'])
        print(proyecto)
        context["sprints"] = proyecto.sprint_set.all()
        context["proyecto"] = proyecto
        context["estado_sprint"] = ['Pendiente','En curso','Finalizado']
        


        return context
    


""" USER STORIES"""
@method_decorator(login_required, name='dispatch')
class CreateSprintView( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'sprints/create_sprint.html'
    model = Sprint
    success_url = '/sprints/'
    form_class = SprintForm

    def get_form_kwargs(self):
        kwargs = super(CreateSprintView, self).get_form_kwargs()
        
        proyecto = Proyecto.objects.filter(pk=self.kwargs['pk']).first()
       
        print(self.kwargs['pk'])

        kwargs['proyecto'] =proyecto # pasamos el backlog a los kwargs del formulario
        return kwargs

    def get_success_url(self):
        
        return reverse('list_sprints',args=(self.kwargs['pk'],))
    
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        print(self.kwargs['pk'])
        proyecto = Proyecto.objects.filter(pk=self.kwargs['pk']).first()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        context["proyecto"] = proyecto
       


        return context
    def form_valid(self, form):
        
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class UpdateSprintView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'sprints/update_sprint.html'
    model = Sprint
    success_url = '/sprints/'
    form_class = SprintUpdateForm


    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos

        return context


@method_decorator(login_required, name='dispatch')
class DetailSprintView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Sprint
    template_name = 'sprints/detail_sprint.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        userstories= UserStory.objects.filter(sprint_id=self.kwargs['pk'])
        print(userstories)
        context["object_list"] = userstories
        context["pk"] = self.kwargs['pk']

        us_pendientes=0
        """Verificar si hay userstories en estado terminado"""
        for us in userstories:
            if us.estado == 1 or us.estado == 2:
                us_pendientes+=1
        
        context["us_pendientes"]= us_pendientes

        return context

def iniciar_sprint(request, pk):
    sprint = Sprint.objects.filter(pk=pk).first()
    sprint.estado = 1
    sprint.save()
    return reverse('list_sprints',args=(self.kwargs['pk'],))

def terminar_sprint(request, pk):
    sprint = Sprint.objects.filter(pk=pk).first()
    sprint.estado = 2
    sprint.save()
    return reverse('list_sprints',args=(self.kwargs['pk'],))


@method_decorator(login_required, name='dispatch')
class DeleteSprintView( LoginRequiredMixin, DeleteView):
    model= Sprint
    success_url= ''
    template_name= 'sprints/delete_sprint.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
       


        return context
    def get_success_url(self):
        
        return reverse('list_sprints',args=(self.kwargs['pk'],))
    
    def form_valid(self, form):
        
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
@method_decorator(login_required, name='dispatch')
class KanbanView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Sprint
    template_name = 'sprints/kanban.html'
    def get_context_data(self, **kwargs):
        permisos=[]
        user = self.request.user
        permisos = user.get_permisos()
        print(permisos)
       

        
        context = super().get_context_data(**kwargs)
        context["permisos"] = permisos
        userstories= UserStory.objects.filter(sprint_id=self.kwargs['pk'])
        print(userstories)
        context["object_list"] = userstories
        context["pk"] = self.kwargs['pk']
        print(self.kwargs['pk'])

        return context
