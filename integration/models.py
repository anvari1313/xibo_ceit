from django.db import models


# Model of displays
class Display(models.Model):
    display_id = models.IntegerField(primary_key=True)
    display = models.CharField(max_length=300)
    client_address = models.CharField(max_length=15, null=True)


class Widget(models.Model):
    widget_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, default="text")
    type = models.CharField(max_length=20)


class Course(models.Model):
    name = models.CharField(max_length=300)


class Task(models.Model):
    task_datetime = models.DateTimeField
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
    text = models.CharField(max_length=700)
    task_datetime_hour = models.IntegerField(null=True)
    task_datetime_min = models.IntegerField(null=True)


class Layout(models.Model):
    layout_id = models.IntegerField(primary_key=True)
    layout = models.CharField(max_length=300)
