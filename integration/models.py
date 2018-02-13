from django.db import models

# Model of displays
class Display(models.Model):
    display = models.CharField(max_length=300)
