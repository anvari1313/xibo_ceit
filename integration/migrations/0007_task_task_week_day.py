# Generated by Django 2.0.1 on 2018-02-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0006_taskschedule_task_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_week_day',
            field=models.IntegerField(null=True),
        ),
    ]