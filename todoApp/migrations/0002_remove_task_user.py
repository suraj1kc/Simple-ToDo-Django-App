# Generated by Django 4.1.7 on 2023-02-21 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
