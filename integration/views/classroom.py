from django.shortcuts import render, redirect
from django.urls import reverse
from integration.models import ClassRoom
from integration.models import Display
from integration.models import ClassroomSchedule
from django.views import View


class ClassRoomView(View):

    def get(self, request, *args, **kwargs):
        displays = Display.objects.all()
        class_room = ClassRoom.objects.all()

        return render(request, 'integration/class/index.html', {'displays': displays, 'class_rooms': class_room})


class ClassRoomTable(View):

    # For showing the list of classroom time table
    def get(self, request, *args, **kwargs):
        week_days = [
            {'id': 0, 'day': 'شنبه'},
            {'id': 1, 'day': 'یک شنبه'},
            {'id': 2, 'day': 'دو شنبه'},
            {'id': 3, 'day': 'سه شنبه'},
            {'id': 4, 'day': 'چهار شنبه'},
            {'id': 5, 'day': 'پنج شنبه'},
            {'id': 6, 'day': 'جمعه'},
        ]

        classroom_id = kwargs.get('classroom_id', "any_default")
        class_room = ClassRoom.objects.get(id=classroom_id)
        schedules = ClassroomSchedule.objects.filter(classroom=class_room)
        return render(request, 'integration/class/table.html', {'class_room': class_room, 'schedules': schedules,
                                                                'week_days': week_days})

    def post(self, request, *args, **kwargs):
        classroom_id = kwargs.get('classroom_id', "any_default")
        class_room = ClassRoom.objects.get(id=classroom_id)
        start_time_min = request.POST.get('start-time-min')
        start_time_hour = request.POST.get('start-time-hour')
        teacher_name = request.POST.get('teacher-name')
        subject_name = request.POST.get('subject-name')
        week_day = request.POST.get('week-day')
        classroom_schedule = ClassroomSchedule()
        return redirect(reverse('classroom.class_id', args=[classroom_id]))
