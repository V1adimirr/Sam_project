from django import forms

from .models import TaskModel


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['description', 'status', 'real_date']
        widgets = {
            'real_date': forms.SelectDateWidget
        }

