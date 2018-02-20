from django.http import JsonResponse
import time
from xibo.requests import XiboRest


def tick(request):
    str = '<p style=\"text-align: center;\"><font color=\"#ffffff\"><span style=\"fon' \
          't-size: 48px;\">شبکه های غیر کامپیوتری</span></font></p>\r\n\r\n<p style=\"' \
          'text-align: center;\"><font color=\"#ffffff\"><span style=\"font-size: 48px;' \
          '\">دکتر صبایی</span></font></p>\r\n'

    result = XiboRest.update_widget(widget_id=7, text=str)
    return JsonResponse({'NOW': time.time(), 'res': result})
