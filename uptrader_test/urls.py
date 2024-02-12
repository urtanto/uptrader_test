"""
URL configuration for uptrader_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a', index_page, name='a'),  # для теста
    path('b', index_page, name='b'),
    path('c', index_page, name='c'),
    path('d', index_page, name='d'),
    path('e', index_page, name='e'),
    path('f', index_page, name='f'),
    path('', index_page, name='home'),
]
