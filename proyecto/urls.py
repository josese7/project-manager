from django.urls import path
from django.views.generic import TemplateView
from proyecto.views import ProyectoListView, CreateProyectoView, UpdateProyectoView, DeleteProyectoView, DetailProyectoView, ListProyectoUserView, ManageProyectoUserView
""" , AddUserProyectoView, , DeleteUserProyectoView  """


urlpatterns = [
    
    path('', ProyectoListView.as_view(), name="list_proyectos"),
    path('add/', CreateProyectoView.as_view(), name='create_proyecto'),
    path('detail/<int:pk>/', DetailProyectoView.as_view(), name='detail_proyecto'),
    path('edit/<int:pk>/', UpdateProyectoView.as_view(), name='update_proyecto'),
    path('delete/<int:pk>/', DeleteProyectoView.as_view(), name='delete_proyecto'),
    path('detail/<int:pk>/list', ListProyectoUserView.as_view(), name='list_proy_usuario'),
    path('detail/<int:pk>/manage', ManageProyectoUserView.as_view(), name='manage_proy_usuario'),
    
]

""" 
    
    path('detail/<int:pk>/delete', DeleteUserProyectoView.as_view(), name='delete_proy_usuario'), """