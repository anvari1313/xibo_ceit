from django.views import View
from django.shortcuts import render, redirect
from integration.models import Display, TaskSchedule, Widget


class DisplaySelect(View):

    def get(self, request, *args, **kwargs):
        displays = Display.objects.all()
        return render(request, 'integration/timesheet/display.html', {'displays': displays})


class ScheduleDisplay(View):

    def get(self, request, *args, **kwargs):
        display_id = kwargs.get('display_id', "any_default")

        weekdays = [
            {'day':'Sunday', 'dow': 0}, {'day':'Monday', 'dow': 1}, {'day':'Tuesday', 'dow': 2},
            {'day':'wednesday', 'dow': 3}, {'day':'Thursday', 'dow': 4}, {'day':'Friday', 'dow': 5},
            {'day':'Saturday', 'dow': 6}]
        timeslots = [
            {'start': '7:45', 'end': '9:15'},
            {'start': '9:15', 'end': '10:45'},
            {'start': '10:45', 'end': '12:15'},
            {'start': '12:15', 'end': '13:30'},
            {'start': '13:30', 'end': '15'},
            {'start': '15', 'end': '16:30'},
        ]
        return render(request, 'integration/timesheet/time-table.html', {
            'weekdays': weekdays,
            'timeslots': timeslots,
            'display_id': display_id
        })


class ScheduleContent(View):

    def get(self, request, *args, **kwargs):
        print('This is code')
        timeslot = self.request.GET.get('timeslot')
        dow = self.request.GET.get('dow')
        widgets = Widget.objects.all()

        return render(request, 'integration/timesheet/parameter-set.html', {
            'display_id': kwargs.get('display_id'),
            'timeslot': timeslot,
            'dow': dow,
            'widgets': widgets
        })

    def post(self, request, *args, **kwargs):
        display_id = kwargs.get('display_id')
        timeslot = request.POST.get('timeslot')
        dow = request.POST.get('dow')

        widget_id = request.POST.get('widget_id')
        text = request.POST.get('text')
        hours, minutes = map(int, timeslot.split(':'))
        widget = Widget(widget_id=widget_id)
        task_schedule = TaskSchedule(widget=widget, task_datetime_min=minutes,
                                     task_datetime_hour=hours, task_week_day=dow, text=text)
        task_schedule.save()
        return redirect('/timesheet/display/' + str(display_id) + '/')
