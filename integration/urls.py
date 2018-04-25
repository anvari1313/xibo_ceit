from django.conf.urls import url
from django.urls import path


from . import controller
from .controller import Display
from .views.xibo import Xibo
from .views.user import login_user
from .views.home import Home
from .views.tick import MinuteTicker
from .views.task import Task, TaskListView
from .views.timesheet import DisplaySelect, ScheduleDisplay, ScheduleContent
from .views.timeslice import ClassTimeSliceView
from .views.classtimesheet import ClassTimeSheet
from django.views.generic import TemplateView
from .views.classroom import ClassRoomView, ClassRoomTable
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
    url(r'tick/every/minute/$', MinuteTicker.as_view(), name='tick.minute'),

    url(r'task/$', method_dispatch(GET=TaskListView.as_view()), name='task.index'),
    url(r'task/new/$', method_dispatch(
        GET=TemplateView.as_view(template_name="integration/task/schedule.html"),
        POST=Task.new
    ), name='task.new'),
    url(r'timesheet/$', DisplaySelect.as_view(), name="timesheet.selectdisplay"),
    path('timesheet/display/<int:display_id>/', ScheduleDisplay.as_view(), name="timesheet.tabletime"),
    path('timesheet/display/<int:display_id>/content/', ScheduleContent.as_view(), name="timesheet.content"),
    path('class/table/', ClassTimeSheet.as_view(), name="somenameforpath"),
    path('admin/timeslice/class/', ClassTimeSliceView.as_view(), name="timeslice.class"),
    path('classroom/<int:classroom_id>/', ClassRoomTable.as_view(), name="classroom.class_id"),
    path('admin/classroom/', ClassRoomView.as_view(), name='classroom.index')
]
