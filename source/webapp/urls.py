from django.urls import path

from .views import TaskView, TaskCreate, TaskDelete, TaskUpdate, TaskDetail

urlpatterns = [

    path('', TaskView.as_view(), name='index'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),

]