from django.shortcuts import render, redirect
from django.urls import reverse
from integration.models import ClassRoom
from integration.models import Display
from integration.models import Widget
from integration.models import ClassroomSchedule
from integration.models import week_days_arr
from django.views import View
from django.http import Http404
from django.core.files.storage import FileSystemStorage


class BulkClassScheduling(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'integration/class/bulk.html')
        else:
            return redirect(reverse("user.login"))

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        if request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'integration/class/bulk.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'admin/404.html')


class ClassRoomView(View):

    def get(self, request, *args, **kwargs):
        # displays = Display.objects.all()
        # class_room = ClassRoom.objects.all()
        #
        # displays = Display.objects.all()
        # teacher_name_widgets = Widget.objects.all()
        # subject_name_widgets = Widget.objects.all()
        # return render(request, 'integration/class/index.html', {
        #     'displays': displays,
        #     'class_rooms': class_room,
        #     'teacher_name_widgets': teacher_name_widgets,
        #     'subject_name_widgets': subject_name_widgets
        # })
        if request.user.is_authenticated:
            class_displays = Display.objects.filter(is_in_hallway=False).order_by('display_id')
            print(class_displays)
            return render(request, 'integration/class/index.html', {
                'class_displays': class_displays,
            })
        else:
            return redirect(reverse("user.login"))

    def post(self, request, *args, **kwargs):
        name = request.POST.get('classroom-name')
        display_id = request.POST.get('display-id')
        teacher_name_widget_id = request.POST.get('teacher-name-widget')
        subject_name_widget_id = request.POST.get('subject-name-widget')

        display = Display.objects.get(display_id=display_id)
        teacher_name_widget = Widget.objects.get(widget_id=teacher_name_widget_id)
        subject_name_widget = Widget.objects.get(widget_id=subject_name_widget_id)

        classroom = ClassRoom(name=name, display=display,
                              teacher_name_widget=teacher_name_widget, subject_name_widget=subject_name_widget)
        classroom.save()
        return redirect(reverse('classroom.index'))



class ClassRoomTable(View):

    # For showing the list of classroom time table
    def get(self, request, *args, **kwargs):

        _week_days = [
            {'id': 0, 'day': 'شنبه'},
            {'id': 1, 'day': 'یک شنبه'},
            {'id': 2, 'day': 'دو شنبه'},
            {'id': 3, 'day': 'سه شنبه'},
            {'id': 4, 'day': 'چهار شنبه'},
            {'id': 5, 'day': 'پنج شنبه'},
            {'id': 6, 'day': 'جمعه'},
        ]
        # for i in range(_week_days):
        #     print(i)

        classroom_id = kwargs.get('classroom_id', "any_default")
        try:
            class_room = ClassRoom.objects.get(id=classroom_id)
        except ClassRoom.DoesNotExist:
            raise Http404

        schedules = ClassroomSchedule.objects.filter(classroom=class_room)
        return render(request, 'integration/class/table.html', {'class_room': class_room, 'schedules': schedules,
                                                                'week_days': _week_days})

    def post(self, request, *args, **kwargs):
        classroom_id = kwargs.get('classroom_id', "any_default")
        try:
            class_room = ClassRoom.objects.get(id=classroom_id)
        except ClassRoom.DoesNotExist:
            raise Http404

        start_time = request.POST.get('start-time')
        start_time_hour = start_time.split(':')[0]
        start_time_min = start_time.split(':')[1]
        teacher_name = request.POST.get('teacher-name')
        subject_name = request.POST.get('subject-name')
        week_day = request.POST.get('week-day')
        classroom_schedule = ClassroomSchedule(start_time_hour=start_time_hour,
                                               start_time_min=start_time_min,
                                               teacher_name=teacher_name,
                                               subject_name=subject_name,
                                               week_day=week_day,
                                               classroom=class_room)
        classroom_schedule.save()
        return redirect(reverse('classroom.class_id', args=[classroom_id]))


class ClassRoomTableThesis(View):
    # For showing the list of classroom time table
    def get(self, request, *args, **kwargs):

        _week_days = [
            {'id': 0, 'day': 'شنبه'},
            {'id': 1, 'day': 'یک شنبه'},
            {'id': 2, 'day': 'دو شنبه'},
            {'id': 3, 'day': 'سه شنبه'},
            {'id': 4, 'day': 'چهار شنبه'},
            {'id': 5, 'day': 'پنج شنبه'},
            {'id': 6, 'day': 'جمعه'},
        ]
        # for i in range(_week_days):
        #     print(i)

        classroom_id = kwargs.get('classroom_id', "any_default")
        try:
            class_room = ClassRoom.objects.get(id=classroom_id)
        except ClassRoom.DoesNotExist:
            raise Http404

        schedules = ClassroomSchedule.objects.filter(classroom=class_room)
        return render(request, 'integration/class/thesis.html', {'class_room': class_room, 'schedules': schedules,
                                                                'week_days': _week_days})