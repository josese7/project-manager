from django.urls import path, include
from django.views.generic import TemplateView
from securitytest.views import SecurityView

urlpatterns = [
    
    path('', SecurityView.as_view(), name="security"),
    path('roles/', include('rol.urls')),
    path('usuarios/', include('usuarios.urls')),
    
]