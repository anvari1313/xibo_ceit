from django.shortcuts import render, redirect
from django.urls import reverse


class Home:
    @staticmethod
    def index(request):
        if request.user.is_authenticated:
            return render(request, 'integration/index.html', {'user': {'name': 'user1'}})
        else:
            return redirect(reverse("user.login"))
