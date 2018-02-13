from django.http import HttpResponse
from django.shortcuts import render
from xibo.requests import XiboRest


def index(request):
    return render(request, 'integration/home.html', {'time': '22:03 GMT'})


class Display:
    @staticmethod
    def index(request):
        r = XiboRest.get_all_displays()
        print(r)
        return render(request, 'integration/display/index.html', {'displays': r})


def sync(request):
    r = XiboRest.get_time()

    return render(request, 'integration/index.html',  r)
