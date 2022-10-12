from django.contrib import admin

from .models import TaskModel, TaskStatus, TaskType


class TaskAdmin(admin.ModelAdmin):
    fields = ['task_name', 'description', 'status', 'type']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(TaskModel, TaskAdmin)


class TaskStatusAdmin(admin.ModelAdmin):
    fields = ['status_name']


admin.site.register(TaskStatus, TaskStatusAdmin)


class TaskTypeAdmin(admin.ModelAdmin):
    fields = ['type_name']


admin.site.register(TaskType, TaskTypeAdmin)
