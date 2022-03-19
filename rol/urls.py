from django.urls import path
from django.views.generic import TemplateView
from rol.views import RolListView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="base.html")),
    path('list/', RolListView.as_view(), name="lits-rol"),
]