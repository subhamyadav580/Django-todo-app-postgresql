# Generated by Django 3.0.5 on 2020-06-07 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addtodo', '0003_auto_20200607_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='datetime',
        ),
    ]
