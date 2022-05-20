from django.urls import path
from django.views.generic import TemplateView
from backlog.views import ListBacklogView, UpdateBacklogView, DetailBacklogView, CreateUserStoryView, UpdateUserStoryView, DeleteUserStoryView, UpdateUserStoryView, DetailUserStoryView


urlpatterns = [
    
    path('', ListBacklogView.as_view(), name="list_backlogs"),
    path('edit/<int:pk>/', UpdateBacklogView.as_view(), name='update_backlog'),
    path('detail/<int:pk>/', DetailBacklogView.as_view(), name='detail_backlog'),
    path('<int:pk>/addus/', CreateUserStoryView.as_view(), name='create_us'),
    path('editus/<int:pk>/', UpdateUserStoryView.as_view(), name='update_userstory'),
    path('deleteus/<int:pk>/', DeleteUserStoryView.as_view(), name='delete_userstory'),
    path('detailus/<int:pk>/', DetailUserStoryView.as_view(), name='detail_userstory'),

]

""" 
    
    path('detail/<int:pk>/delete', DeleteUserProyectoView.as_view(), name='delete_proy_usuario'), """