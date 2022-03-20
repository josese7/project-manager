from django.urls import path
from django.views.generic import TemplateView
from rol.views import ListRolView, CreateRolView, UpdateRolView, DeleteRolView, DetailRolView


urlpatterns = [
    
    path('', ListRolView.as_view(), name="list_rol"),
    path('add/', CreateRolView.as_view(), name='create_rol'),
    path('edit/<int:pk>/', UpdateRolView.as_view(), name='update_rol'),
    path('delete/<int:pk>/', DeleteRolView.as_view(), name='delete_rol'),
    path('detail/<int:pk>/', DetailRolView.as_view(), name='detail_rol'),
]
