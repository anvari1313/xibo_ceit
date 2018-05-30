from django.shortcuts import render, redirect
from integration.models import Display
from django.views import View
from django.http import Http404
from django.urls import reverse


class DisplayView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            displays = Display.objects.all()

            return render(request, 'integration/display/index.html', {
                'displays': displays,
            })
        else:
            return redirect(reverse("user.login"))


class DisplayAliasView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            display_id = kwargs.get('display_id', "any_default")
            try:
                display = Display.objects.get(display_id=display_id)
            except Display.DoesNotExist:
                raise Http404
            alias_name = request.POST.get('alias-name')
            display.alias = alias_name
            display.save(update_fields=['alias'])

            return redirect(reverse('display.index'))
        else:
            return redirect(reverse("user.login"))
