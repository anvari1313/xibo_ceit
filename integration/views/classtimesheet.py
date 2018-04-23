from django.views import View
from django.shortcuts import render, redirect
from integration.models import ClassTimeSlice


class ClassTimeSheet(View):

    def get(self, request, *args, **kwargs):
        time_slices = ClassTimeSlice.objects.all()
        print(time_slices)
        week_days = [
            {'id': 0, 'day': 'شنبه'},
            {'id': 1, 'day': 'یک شنبه'},
            {'id': 2, 'day': 'دو شنبه'},
            {'id': 3, 'day': 'سه شنبه'},
            {'id': 4, 'day': 'چهار شنبه'},
            {'id': 5, 'day': 'پنج شنبه'},
            {'id': 6, 'day': 'جمعه'},
        ]
        return render(request, "integration/class/table.html",
                      {
                          'timeslices': time_slices,
                          'week_days': week_days
                      })

    def post(self, request, *args, **kwargs):
        s_time = request.POST.get('start-time')
        e_time = request.POST.get('end-time')
        time_slice = ClassTimeSlice(start_time=s_time, end_time=e_time)
        time_slice.save()
        return redirect('/admin/timeslice/class/')
