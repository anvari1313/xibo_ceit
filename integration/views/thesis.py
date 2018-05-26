from django.views import View
from django.shortcuts import render, redirect
from integration.models import Display


class ThesisView(View):
    def get(self, request, *args, **kwargs):
        displays = Display.objects.all()
        return render(request,
                      'integration/thesis/index.html',
                      {
                          'displays': displays
                      }
                      )