from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import TaskCreateForm
from .models import TaskModel


class TaskView(ListView):
    model = TaskModel
    template_name = 'index.html'
    context_object_name = 'tasks'


class TaskCreate(CreateView):
    form_class = TaskCreateForm
    template_name = 'task_create.html'

    def get_success_url(self):
        return reverse('index')


class TaskDelete(DeleteView):
    model = TaskModel
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')
    context_object_name = 'task'


class TaskUpdate(UpdateView):
    model = TaskModel
    form_class = TaskCreateForm
    template_name = 'task_update.html'

    def get_success_url(self):
        return reverse('index')
