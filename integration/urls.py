from django.conf.urls import url
from . import views
from .views import Display
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="integration/index.html")),
    url(r'display/$', Display.index, name='index'),
    url(r'sync/$', views.sync, name='sync')
]
