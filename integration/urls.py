from django.conf.urls import url
from . import controller
from .controller import Display
from .views.xibo import Xibo
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="integration/index.html")),
    url(r'xibo/$', Xibo.index, name='xibo.index'),
    url(r'display/$', Display.index, name='index'),
    url(r'sync/$', controller.sync, name='sync')
]
