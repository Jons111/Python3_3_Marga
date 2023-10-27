from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminServise(admin.ModelAdmin):
    list_display = ["id", 'name', 'text', 'image', 'data']

admin.site.register(Servise, AdminServise)

class AdminProjects(admin.ModelAdmin):
    list_display = ['id', 'name', 'adres', 'image', 'data']

admin.site.register(Project, AdminProjects)

class AdminHome(admin.ModelAdmin):
    list_display = ["id", 'name', 'text', 'image', 'data']

admin.site.register(Home, AdminHome)
