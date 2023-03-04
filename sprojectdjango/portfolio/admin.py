from django.contrib import admin
from .models import Project 

class ProjectAdmin(admin.ModelAdmin): #mostramos solo lectura los campos creacion y modificacion
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
