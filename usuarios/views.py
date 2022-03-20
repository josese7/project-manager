from django.shortcuts import render
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


from usuarios.models import Usuario
# Create your views here.
@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model= Usuario
    template_name= 'usuarios/list_user.html'

@method_decorator(login_required, name='dispatch')
class DetailUserView(LoginRequiredMixin, DetailView):
    """
    Clase de la vista de los detalles de un Usuario
    """
    model = Usuario
    template_name = 'usuarios/detail_user.html'

@method_decorator(login_required, name='dispatch')
class CreateUserView( LoginRequiredMixin, CreateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'usuarios/create_user.html'
    model = Usuario
    success_url = 'security/usuarios/'
    form_class = CreateUserForm
    success_message = 'Se ha creado el usuario'

@method_decorator(login_required, name='dispatch')
class UpdateUserView( LoginRequiredMixin, UpdateView):
    """
    Clase de la vista para la creacion de un Usuario
    """
    template_name = 'usuarios/update_user.html'
    model = Usuario
    success_url = 'security/usuarios/'
    form_class = UpdateUserForm
    success_message = 'Se ha modificado el usuario'

@method_decorator(login_required, name='dispatch')
class DeleteUserView( LoginRequiredMixin, DeleteView):
    model= Usuario
    success_url= 'security/usuarios/'
    template_name= 'usuarios/delete_user.html'