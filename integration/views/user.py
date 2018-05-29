from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class UserLoginView(View):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'integration/user/login.html')

    def get(self, request, *args, **kwargs):
        return render(request, 'integration/user/login.html')


class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("user.login"))
