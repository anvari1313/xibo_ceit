# Generated by Django 2.0.1 on 2018-03-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0008_taskschedule_task_week_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTimeSlice',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
