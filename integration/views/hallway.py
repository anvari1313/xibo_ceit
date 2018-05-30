from django.shortcuts import render, redirect
from integration.models import Display
from django.views import View
from django.http import Http404
from django.urls import reverse


class HallwayPropagationThesisView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            hallway_displays = Display.objects.filter(is_in_hallway=True).order_by('display_id')

            return render(request, 'integration/hallway/propagation/thesis.html', {
                'hallway_displays': hallway_displays,
            })
        else:
            return redirect(reverse("user.login"))


class DisplayEditView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            display_id = kwargs.get('display_id', "any_default")
            try:
                display = Display.objects.get(display_id=display_id)
            except Display.DoesNotExist:
                raise Http404
            alias_name = request.POST.get('alias-name')
            is_in_hall = request.POST.get('is-in-hall')
            if is_in_hall is None:
                display.is_in_hallway = False
            else:
                display.is_in_hallway = True

            display.alias = alias_name
            display.save(update_fields=['alias', 'is_in_hallway'])

            return redirect(reverse('display.index'))
        else:
            return redirect(reverse("user.login"))
