from django.shortcuts import render, redirect
from django.views import generic
from integration.models import Task
import datetime


class TaskListView(generic.ListView):
    model = Task
    template_name = 'integration/task/index.html'


class Task:
    @staticmethod
    def new(request):
        widget_id = request.POST['widget-id']
        _datetime = request.POST['datetime']
        text = request.POST['text']
        task_obj = Task()
        task_obj.widget_id = widget_id
        task_obj.text = text
        task_obj.task_datetime = datetime.datetime.now()
        task_obj.save()
        return redirect('/task')
