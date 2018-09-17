# from auth.views.login import Home, view_function
from .views.login import UserLoginView
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('user/login', UserLoginView.as_view(), name="auth.user.login"),
    # url(r'^$', ),
]
