# Generated by Django 2.0.1 on 2018-05-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0018_display_is_in_hallway'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallwayPropagationThesisSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=120)),
                ('teacher_name', models.CharField(max_length=120)),
                ('judge_teacher_name1', models.CharField(max_length=120)),
                ('judge_teacher_name2', models.CharField(max_length=120, null=True)),
                ('judge_teacher_name3', models.CharField(max_length=120, null=True)),
                ('holding_year', models.IntegerField()),
                ('holding_month', models.IntegerField()),
                ('holding_day', models.IntegerField()),
                ('holding_hour', models.IntegerField()),
                ('holding_minute', models.IntegerField()),
            ],
        ),
    ]