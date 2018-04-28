from django.http import JsonResponse
from django.views import View

from xibo.requests import XiboRest
from integration.models import TaskSchedule
from integration.models import ClassRoom, ClassroomSchedule

import datetime


def tick(request):
    now = datetime.datetime.now()
    schedule_lists = TaskSchedule.objects.filter(task_datetime_hour=now.hour, task_datetime_min=now.minute)
    for schedule in schedule_lists:
        XiboRest.update_widget(widget_id=schedule.widget.widget_id, text=schedule.text)

    return JsonResponse({'NOW': now})


class MinuteTicker(View):
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        dow = now.weekday()
        schedule_lists = TaskSchedule.objects.filter(
            task_datetime_hour=now.hour,
            task_datetime_min=now.minute,
            task_week_day=dow
        )
        for schedule in schedule_lists:
            XiboRest.update_widget(widget_id=schedule.widget.widget_id, text=schedule.text)

        classroom_schedules = ClassroomSchedule.objects.filter(
            start_time_hour=now.hour,
            start_time_min=now.minute,
            week_day=dow)

        updated_widgets = []

        for classroom_schedule in classroom_schedules:
            teacher_widget_id = classroom_schedule.classroom.teacher_name_widget.widget_id
            teacher_name = classroom_schedule.teacher_name
            subject_widget_id = classroom_schedule.classroom.subject_name_widget.widget_id
            subject_name = classroom_schedule.subject_name
            XiboRest.update_widget(
                widget_id=teacher_widget_id,
                text=teacher_name)
            XiboRest.update_widget(
                widget_id=subject_widget_id,
                text=subject_name)

            updated_widgets.append({
                'TEACHER':{
                    'widget_id': teacher_widget_id,
                    'widget_text': teacher_name
                },
                'SUBJECT': {
                    'widget_id': subject_widget_id,
                    'widget_text': subject_name
                }})
            print('T: ' + str(classroom_schedule.classroom.teacher_name_widget.widget_id) +
                  ', ' + classroom_schedule.teacher_name)
            print('S: ' + str(classroom_schedule.classroom.subject_name_widget.widget_id) +
                  ', ' + classroom_schedule.subject_name)
            print()

        return JsonResponse({'NOW': now, 'DOW': dow, 'UPDATED_WIDGETS': updated_widgets})
