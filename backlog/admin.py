from django.contrib import admin
from .models import Backlog, UserStory, Comentario

# Register your models here.
admin.site.register(Backlog)
admin.site.register(UserStory)
admin.site.register(Comentario)