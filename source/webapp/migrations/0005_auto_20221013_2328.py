# Generated by Django 4.1.2 on 2022-10-13 17:28

from django.db import migrations

def transfer_tags(apps, schema_editor):
    Article = apps.get_model('webapp.TaskModel')
    for article in Article.objects.all():
        article.type.add(article.type_old)

def rollback_transfer(apps, schema_editor):
    Article = apps.get_model('webapp.TaskModel')
    for article in Article.objects.all():
        article.type_old.add(article.type.all())


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_taskmodel_type'),
    ]

    operations = [
        migrations.RunPython(transfer_tags, rollback_transfer)
    ]