# Generated by Django 4.1.2 on 2022-10-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_taskmodel_type_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='type',
            field=models.ManyToManyField(related_name='types', to='webapp.tasktype', verbose_name='Тип'),
        ),
    ]
