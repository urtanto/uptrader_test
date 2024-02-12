from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_page(request: WSGIRequest):
    """
    Renders all test pages
    """
    context = {
        "pagename": request.path.split("/")[-1],
    }
    return render(request, 'base.html', context)
