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
    task_week_day = models.IntegerField(null=True)

    def __str__(self):
        return 'text : ' + self.text


class TaskSchedule(models.Model):
    task_datetime = models.DateTimeField(null=True)
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)
    text = models.CharField(max_length=700)
    task_datetime_hour = models.IntegerField(null=True)
    task_datetime_min = models.IntegerField(null=True)
    task_week_day = models.IntegerField(null=True)

    def __str__(self):
        return 'text : ' + self.text


class Layout(models.Model):
    layout_id = models.IntegerField(primary_key=True)
    layout = models.CharField(max_length=300)


class ClassTimeSlice(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time.hour) + ':' + str(self.start_time.minute) \
               + ' - ' + str(self.end_time.hour) + ':' + str(self.end_time.minute)


class ClassRoom(models.Model):
    name = models.CharField(max_length=200)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    teacher_name_widget = models.ForeignKey(Widget, on_delete=models.CASCADE,
                                            related_name='teacher_name_widget', null=True)
    subject_name_widget = models.ForeignKey(Widget, on_delete=models.CASCADE,
                                            related_name='subject_name_widget', null=True)
    
    def __str__(self):
        return 'name: ' + str(self.name) + ', display'


class ClassroomSchedule(models.Model):
    teacher_name = models.CharField(max_length=200)
    subject_name = models.CharField(max_length=400)
    week_day = models.IntegerField()
    start_time_min = models.IntegerField()
    start_time_hour = models.IntegerField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return 'Teacher Name: ' + self.teacher_name

