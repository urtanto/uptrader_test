from django.contrib import admin
from main.models import *


@admin.register(Menu)
class AllRootUrl(admin.ModelAdmin):
    list_display = ("id", "name", "parent")


@admin.register(Url)
class AllChildUrl(admin.ModelAdmin):
    list_display = ("id", "name_url", "parent")
