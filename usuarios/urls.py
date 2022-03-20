from django.urls import path
from django.views.generic import TemplateView
from usuarios.views import UserListView, CreateUserView, UpdateUserView, DeleteUserView, DetailUserView


urlpatterns = [
    
    path('', UserListView.as_view(), name="list_users"),
    path('add/', CreateUserView.as_view(), name='create-user'),
    path('detail/<int:pk>/', DetailUserView.as_view(), name='detail_user'),
    path('edit/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
]
