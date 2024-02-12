from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from main.models import *


def base_root_url(func):
    def wrapper(request, *args, **kwargs):
        if len(RootUrl.objects.all()) == 0:
            root_url = RootUrl(url="/")
            root_url.save()
        return func(request, *args, **kwargs)

    return wrapper


@base_root_url
def index_page(request: WSGIRequest):
    context = {
        "url": request.build_absolute_uri().split("/")[3:],
        "pagename": request.build_absolute_uri().split("/")[-1],
    }
    return render(request, 'base.html', context)
