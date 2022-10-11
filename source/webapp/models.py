from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class TaskModel(models.Model):
    description = models.CharField(max_length=100, verbose_name='Описание')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0],
                              verbose_name='Статус')
    real_date = models.DateField(null=True, blank=True, verbose_name='Время выполнения')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        db_table = 'TaskModel'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

