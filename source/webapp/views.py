from django.shortcuts import render, get_object_or_404

from .models import TaskModel


def index(request):
    tasks = TaskModel.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)
