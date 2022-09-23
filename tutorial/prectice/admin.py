from django.contrib import admin

from .models import Project, Task

class PrecticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, PrecticeAdmin)
admin.site.register(Task, PrecticeAdmin)