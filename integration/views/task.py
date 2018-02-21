from django.shortcuts import render, redirect
from django.views import generic
from integration.models import TaskSchedule, Widget
import datetime


class TaskListView(generic.ListView):
    model = TaskSchedule
    template_name = 'integration/task/index.html'


class Task:
    @staticmethod
    def new(request):
        widget = Widget.objects.get(widget_id=int(request.POST['widget-id']))
        hour = int(request.POST['hour'])
        minute = int(request.POST['minute'])
        text = request.POST['text']
        task_obj = TaskSchedule(widget=widget, text=text, task_datetime_hour=hour, task_datetime_min=minute)

        r = task_obj.save()

        return redirect('/task')
