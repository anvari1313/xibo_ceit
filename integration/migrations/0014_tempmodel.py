# Generated by Django 2.0.1 on 2018-05-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0013_auto_20180423_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=200)),
            ],
        ),
    ]
