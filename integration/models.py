from django.db import models


# Model of displays
class Display(models.Model):
    display_id = models.IntegerField(primary_key=True)
    display = models.CharField(max_length=300)
    client_address = models.CharField(max_length=15, null=True)


class Widget(models.Model):
    widget_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)


class Course(models.Model):
    name = models.CharField(max_length=300)


class Task(models.Model):
    datetime = models.DateTimeField
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
    text = models.CharField(max_length=700)