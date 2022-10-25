from django import forms

from .models import TaskModel


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task_name', 'description', 'status', 'type']
        widgets = {
            'status': forms.RadioSelect,
            'type': forms.CheckboxSelectMultiple
        }

