from django.http import HttpResponse
from django.shortcuts import render
from xibo.requests import XiboRest
from task.task import task1


def index(request):
    return render(request, 'integration/home.html', {'time': '22:03 GMT'})


class Xibo:
    @staticmethod
    def index(request):
        layouts = XiboRest.get_all_layouts()
        print(layouts)
        displays = XiboRest.get_all_displays()
        print(displays)
        return render(request, 'integration/xibo/index.html', {'layouts': layouts, 'displays': displays})


class Display:
    @staticmethod
    def index(request):
        r = XiboRest.get_all_displays()
        print(r)
        return render(request, 'integration/xibo/display/index.html', {'displays': r})


def sync(request):
    task1(12, repeat=1)
    r = XiboRest.get_time()

    return render(request, 'integration/index.html',  r)
