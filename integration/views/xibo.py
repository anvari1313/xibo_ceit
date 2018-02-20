from xibo.requests import XiboRest
from django.shortcuts import render


class Xibo:
    @staticmethod
    def index(request):
        layouts = XiboRest.get_all_layouts()
        print(layouts)
        displays = XiboRest.get_all_displays()
        print(displays)
        return render(request, 'integration/xibo/index.html', {'layouts': layouts, 'displays': displays})
