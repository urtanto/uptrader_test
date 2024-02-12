from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render



def index_page(request: WSGIRequest):
    context = {
        "url": "/".join(request.path.split("/")[1:]),
        "pagename": request.path.split("/")[-1],
    }
    return render(request, 'base.html', context)
