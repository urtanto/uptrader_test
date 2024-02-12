from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_page(request: WSGIRequest):
    context = {
        "url": "/" + request.build_absolute_uri(),
        "pagename": request.build_absolute_uri().split("/")[-1],
    }
    return render(request, 'base.html', context)
