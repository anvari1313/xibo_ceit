from django.conf.urls import url
from django.urls import path
from .controller import Display
from .views.xibo import Xibo
from .views.user import UserLoginView, UserLogoutView
from .views.home import Home
from .views.tick import MinuteTicker
from .views.template_text import TemplateTextView
from .views.thesis import ThesisView
from django.views.generic import TemplateView
from .views.classroom import ClassRoomView, ClassRoomTable, ClassRoomTableThesis
from util.http_helper import method_dispatch


urlpatterns = [
    url(r'^$', Home.index, name="home.index"),
    url(r'xibo/$', Xibo.index, name='xibo.index'),
    url(r'xibo/update/widget$', method_dispatch(GET=Xibo.update_widget), name='xibo.update.widget'),
    url(r'xibo/update/layout$', method_dispatch(GET=Xibo.update_layout), name='xibo.update.layout'),
    url(r'xibo/update/display', method_dispatch(GET=Xibo.update_display), name='xibo.update.display'),

    url(r'display/$', Display.index, name='index'),

    url(r'user/login/$', UserLoginView.as_view(), name='user.login'),
    url(r'user/logout/$', UserLogoutView.as_view(), name='user.logout'),


    url(r'tick/every/minute/$', MinuteTicker.as_view(), name='tick.minute'),
    path('classroom/rclass/<int:classroom_id>/', ClassRoomTable.as_view(), name="classroom.class_id"),
    path('classroom/thesis/<int:classroom_id>/', ClassRoomTableThesis.as_view(), name="thesis.class_id"),
    path('admin/classroom/', ClassRoomView.as_view(), name='classroom.index'),
    path('admin/templatetext/', TemplateTextView.as_view(), name='templatetext.index'),
    path('thesis/', ThesisView.as_view(), name='thesis'),
    url(r'ad/$', method_dispatch(
        GET=TemplateView.as_view(template_name="integration/home.html")), name='user.not'),
]
