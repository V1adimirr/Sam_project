from django.contrib import admin

from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    fields = ['description', 'status', 'real_date']


admin.site.register(TaskModel, TaskAdmin)
