# Generated by Django 2.0.1 on 2018-02-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0002_widget_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('layout_id', models.IntegerField(primary_key=True, serialize=False)),
                ('layout', models.CharField(max_length=300)),
            ],
        ),
    ]
