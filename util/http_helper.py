from django.http import HttpResponseNotAllowed
import logging


def method_dispatch(**table):
    def invalid_method(request, *args, **kwargs):
        logging.warning("Method Not Allowed (%s): %s" %(request.method, request.path))
        return HttpResponseNotAllowed(table.keys())

    def d(request, *args, **kwargs):
        handler = table.get(request.method, invalid_method)
        return handler(request, *args, **kwargs)
    return d