from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        abstract = True


class TaskModel(BaseModel):
    task_name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('TaskStatus', on_delete=models.CASCADE, related_name='statuses', verbose_name='Статус')
    type = models.ForeignKey('TaskType', on_delete=models.CASCADE, related_name='types', verbose_name='Тип')

    def __str__(self):
        return f'{self.task_name}, {self.description}'

    class Meta:
        db_table = 'TaskModel'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class TaskType(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='Имя типа')

    def __str__(self):
        return f'{self.type_name}'

    class Meta:
        db_table = 'TaskType'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class TaskStatus(models.Model):
    status_name = models.CharField(max_length=20, verbose_name='Имя статуса')

    def __str__(self):
        return f'{self.status_name}'

    class Meta:
        db_table = 'TaskStatus'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
