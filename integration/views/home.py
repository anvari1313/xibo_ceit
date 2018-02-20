from django.shortcuts import render


class Home:
    @staticmethod
    def index(request):
        return render(request, 'integration/index.html', {'user': {'name': 'user1'}})
