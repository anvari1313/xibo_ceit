from django.http import JsonResponse
from xibo.requests import XiboRest
from integration.models import TaskSchedule
import datetime


def tick(request):
    now = datetime.datetime.now()
    schedule_lists = TaskSchedule.objects.filter(task_datetime_hour=now.hour, task_datetime_min=now.minute)
    for schedule in schedule_lists:
        XiboRest.update_widget(widget_id=schedule.widget.widget_id, text=schedule.text)

    return JsonResponse({'NOW': now})
