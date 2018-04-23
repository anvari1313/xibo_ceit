from django.views import View
from django.shortcuts import render, redirect
from integration.models import ClassTimeSlice


class ClassTimeSliceView(View):

    def get(self, request, *args, **kwargs):
        time_slices = ClassTimeSlice.objects.all()
        return render(request, "integration/timeslice/class.html", {'timeslices': time_slices})

    def post(self, request, *args, **kwargs):
        s_time = request.POST.get('start-time')
        e_time = request.POST.get('end-time')
        time_slice = ClassTimeSlice(start_time='7:45', end_time='9:15')
        time_slice.save()
        return redirect('/admin/timeslice/class/')
