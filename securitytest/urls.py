from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    
    path('', TemplateView.as_view(template_name="modulos/seguridad.html"), name="security"),
    path('roles/', include('rol.urls')),
    path('usuarios/', include('usuarios.urls')),
    
]