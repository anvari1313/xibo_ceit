from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from integration.models import Display


class UploadImage(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            hallway_displays = Display.objects.filter(is_in_hallway=True).order_by('display_id')

            return render(request, 'integration/upload-image/index.html', {
                'hallway_displays': hallway_displays,
            })
        else:
            return redirect(reverse("user.login"))
