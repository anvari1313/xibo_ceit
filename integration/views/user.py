from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'integration/user/logout.html')
