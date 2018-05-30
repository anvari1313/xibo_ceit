from django.db import models

week_days_arr = [
            'شنبه',
            'یک شنبه',
            'دو شنبه',
            'سه شنبه',
            'چهار شنبه',
            'پنج شنبه',
            'جمعه',
        ]


# Model of displays
class Display(models.Model):
    display_id = models.IntegerField(primary_key=True)
    display = models.CharField(max_length=300)
    alias = models.CharField(max_length=300, null=True, default="Room")
    client_address = models.CharField(max_length=15, null=True)
    is_in_hallway = models.NullBooleanField(default=False)


class Widget(models.Model):
    widget_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, default="text")
    type = models.CharField(max_length=20)


class HallwayPropagationThesisSchedule(models.Model):
    student_name = models.CharField(max_length=120)
    teacher_name = models.CharField(max_length=120)
    judge_teacher_name1 = models.CharField(max_length=120)
    judge_teacher_name2 = models.CharField(max_length=120, null=True)
    judge_teacher_name3 = models.CharField(max_length=120, null=True)
    holding_year = models.IntegerField()
    holding_month = models.IntegerField()
    holding_day = models.IntegerField()
    holding_hour = models.IntegerField()
    holding_minute = models.IntegerField()
    place = models.CharField(max_length=120, null=True)


class Course(models.Model):
    name = models.CharField(max_length=300)


class Layout(models.Model):
    layout_id = models.IntegerField(primary_key=True)
    layout = models.CharField(max_length=300)


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

    def get_week_day_name(self):
        return week_days_arr[self.week_day]

    def __str__(self):
        return 'Teacher Name: ' + self.teacher_name
