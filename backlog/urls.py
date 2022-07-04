from django.urls import path
from django.views.generic import TemplateView
from backlog.views import ListBacklogView, UpdateBacklogView, DetailBacklogView, CreateUserStoryView, UpdateUserStoryView, DeleteUserStoryView, UpdateUserStoryView, DetailUserStoryView, CreateComentarioUsNext, CreateComentarioUsBack
from proyecto.views import ProyectoListView
from sprint.views import ListSprintView, CreateSprintView, DetailSprintView, UpdateSprintView, iniciar_sprint, KanbanView, terminar_sprint


urlpatterns = [
    
    path('', ProyectoListView.as_view(), name="list_backlogs"),
    path('edit/<int:pk>/', UpdateBacklogView.as_view(), name='update_backlog'),
    path('detail/<int:pk>/', DetailBacklogView.as_view(), name='detail_backlog'),
    path('<int:pk>/addus/', CreateUserStoryView.as_view(), name='create_us'),
    path('editus/<int:pk>/', UpdateUserStoryView.as_view(), name='update_userstory'),
    path('deleteus/<int:pk>/', DeleteUserStoryView.as_view(), name='delete_userstory'),
    path('detailus/<int:pk>/', DetailUserStoryView.as_view(), name='detail_userstory'),
    path('detailus/<int:pk>/addcomentarus_next/', CreateComentarioUsNext.as_view(), name='comentar_userstory_next'),
    path('detailus/<int:pk>/addcomentarus_back/', CreateComentarioUsBack.as_view(), name='comentar_userstory_back'),
    path('sprint/<int:pk>/', ListSprintView.as_view(), name='list_sprints'),
    path('<int:pk>/createSprint/', CreateSprintView.as_view(), name='create_sprint'),
    path('detailSprint/<int:pk>/', DetailSprintView.as_view(), name='detail_sprint'),
    path('editSprint/<int:pk>/', UpdateSprintView.as_view(), name='update_sprint'),
    path('iniciarSprint/<int:pk>/', iniciar_sprint, name='iniciar_sprint'),
    path('terminarSprint/<int:pk>/', terminar_sprint, name='terminar_sprint'),
    path('kanbanSprint/<int:pk>/', KanbanView.as_view(), name='kanban_sprint'),


]

""" 
    
    path('detail/<int:pk>/delete', DeleteUserProyectoView.as_view(), name='delete_proy_usuario'), """