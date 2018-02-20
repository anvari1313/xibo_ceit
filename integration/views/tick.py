from django.http import JsonResponse
import time


def tick(request):
    return JsonResponse({'NOW': time.time()})
