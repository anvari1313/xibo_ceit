# Generated by Django 2.0.1 on 2018-04-22 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0010_auto_20180302_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('display', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integration.Display')),
            ],
        ),
    ]
