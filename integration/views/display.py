from django.shortcuts import render, redirect
from integration.models import Display
from django.views import View


class DisplayView(View):
    def get(self, request, *args, **kwargs):
        displays = Display.objects.all()

        return render(request, 'integration/display/index.html', {
            'displays': displays,
        })
