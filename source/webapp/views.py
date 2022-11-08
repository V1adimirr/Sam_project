from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from .forms import TaskCreateForm
from .models import TaskModel


class TaskView(ListView):
    model = TaskModel
    template_name = 'index.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = TaskModel
    template_name = 'task_detail.html'
    context_object_name = 'task'


class TaskCreate(PermissionRequiredMixin, CreateView):
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    permission_required = 'webapp:add'

    def get_success_url(self):
        return reverse('webapp:index')


class TaskDelete(DeleteView):
    model = TaskModel
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')
    context_object_name = 'task'


class TaskUpdate(PermissionRequiredMixin, UpdateView):
    model = TaskModel
    form_class = TaskCreateForm
    template_name = 'task_update.html'
    permission_required = 'webapp:change'

    def get_success_url(self):
        return reverse('webapp:index')
