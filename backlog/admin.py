from django.contrib import admin
from .models import Backlog, UserStory

# Register your models here.
admin.site.register(Backlog)
admin.site.register(UserStory)