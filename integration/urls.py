from django.conf.urls import url


from . import controller
from .controller import Display
from .views.xibo import Xibo
from .views.user import login_user
from .views.home import Home
from django.views.generic import TemplateView
from util.http_helper import method_dispatch


urlpatterns = [
    url(r'^$', Home.index),
    url(r'xibo/$', Xibo.index, name='xibo.index'),
    url(r'display/$', Display.index, name='index'),
    url(r'user/login/$', method_dispatch(
        POST=login_user,
        GET=TemplateView.as_view(template_name="integration/user/login.html")), name='user.login'),
    url(r'sync/$', controller.sync, name='sync')
]
