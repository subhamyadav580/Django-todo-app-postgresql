# Generated by Django 3.0.5 on 2020-06-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtodo', '0002_todo_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datetime',
            field=models.TextField(),
        ),
    ]
