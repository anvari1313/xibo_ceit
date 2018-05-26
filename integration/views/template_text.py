from django.views import View
from django.shortcuts import render, redirect


class TemplateTextView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'integration/template-text/index.html')