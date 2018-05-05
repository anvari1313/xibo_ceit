from xibo.requests import XiboRest
from django.urls import reverse
from django.shortcuts import render, redirect
from integration.models import Widget, Display, Layout
import xibo.requests


class Xibo:
    @staticmethod
    def index(request):
        if request.user.is_authenticated:
            layouts = Layout.objects.all()
            displays = Display.objects.all()
            widgets = Widget.objects.all()
            return render(request, 'integration/xibo/index.html', {
                'layouts': layouts,
                'displays': displays,
                'widgets': {
                    'attrs': ['widget_id', 'name', 'type'],
                    'values': widgets
                }})
        else:
            return redirect(reverse('user.login'))

    @staticmethod
    def update_widget(request):
        if request.user.is_authenticated:
            widgets = XiboRest.get_all_widgets()
            for item in widgets:
                widget = Widget(widget_id=item['widgetId'], name=item['name'], type=item['type'])
                widget.save()

            return redirect("/xibo")
        else:
            return redirect(reverse('user.login'))

    @staticmethod
    def update_layout(request):
        if request.user.is_authenticated:
            layouts = XiboRest.get_all_layouts()
            for item in layouts:
                print(item)
                layout = Layout(layout_id=item['layoutId'], layout=item['layout'])
                layout.save()

            return redirect("/xibo")
        else:
            return redirect(reverse('user.login'))

    @staticmethod
    def update_display(request):
        if request.user.is_authenticated:
            displays = XiboRest.get_all_displays()
            for item in displays:
                print(item)
                display = Display(display_id=item['displayId'], display=item['display'],
                                  client_address=item['clientAddress'])
                display.save()

                # widget = Widget(widget_id=item['widgetId'], name=item['name'], type=item['type'])
                # widget.save()

            return redirect("/xibo")
        else:
            return redirect(reverse('user.login'))