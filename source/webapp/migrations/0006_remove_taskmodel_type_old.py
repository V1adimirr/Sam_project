# Generated by Django 4.1.2 on 2022-10-13 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20221013_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskmodel',
            name='type_old',
        ),
    ]
