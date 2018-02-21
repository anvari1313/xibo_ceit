from django.conf.urls import url


from . import controller
from .controller import Display
from .views.xibo import Xibo
from .views.user import login_user
from .views.home import Home
from .views.tick import tick
from .views.task import Task, TaskListView
from django.views.generic import TemplateView
from util.http_helper import method_dispatch


urlpatterns = [
    url(r'^$', Home.index),
    url(r'xibo/$', Xibo.index, name='xibo.index'),
    url(r'xibo/update/widget$', method_dispatch(GET=Xibo.update_widget), name='xibo.update.widget'),
    url(r'xibo/update/layout$', method_dispatch(GET=Xibo.update_layout), name='xibo.update.layout'),
    url(r'xibo/update/display', method_dispatch(GET=Xibo.update_display), name='xibo.update.display'),

    url(r'display/$', Display.index, name='index'),
    url(r'user/login/$', method_dispatch(
        POST=login_user,
        GET=TemplateView.as_view(template_name="integration/user/login.html")), name='user.login'),
    url(r'tick/$', method_dispatch(GET=tick), name='tick'),
    url(r'task/$', method_dispatch(GET=TaskListView.as_view()), name='task.index'),
    url(r'task/new/$', method_dispatch(
        GET=TemplateView.as_view(template_name="integration/task/schedule.html"),
        POST=Task.new
    ), name='task.new')
]
