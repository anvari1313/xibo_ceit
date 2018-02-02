from django.http import HttpResponse
from django.shortcuts import render
from xibo.requests import get_time


def index(request):
    return render(request, 'integration/index.html', {'time': '22:03 GMT'})


def sync(request):
    r = get_time()

    return render(request, 'integration/index.html',  r)
