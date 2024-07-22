from django.contrib import admin

# Register your models here.
from .models import Project, Tool

admin.site.register(Project)
admin.site.register(Tool)