from django.views import View
from django.shortcuts import render, redirect
from integration.models import Display


class DisplaySelect(View):

    def get(self, request, *args, **kwargs):
        displays = Display.objects.all()
        return render(request, 'integration/timesheet/display.html', {'displays': displays})


class ScheduleDisplay(View):

    def get(self, request, *args, **kwargs):
        display_id = kwargs.get('display_id', "any_default")

        weekdays = ['Sunday', 'Monday', 'Tuesday', 'wednesday', 'Thursday', 'Friday', 'Saturday']
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
        return render(request, 'integration/timesheet/parameter-set.html')