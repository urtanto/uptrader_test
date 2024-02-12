from django import template
from django.urls import reverse

from main.models import *
from uptrader_test.urls import urlpatterns

register = template.Library()


def get_members(menu: Menu) -> list:
    members = []
    for i in list(menu.menu_set.all()):
        members.append({
            "is_url": False,
            "name": i.name,
            "members": get_members(i)
        })
    for i in list(menu.url_set.all()):
        members.append({
            "is_url": True,
            "name": i.name,
            "url": i.name_url if "/" in i.name_url else reverse(f'{i.name_url}'),
        })
    return members


@register.inclusion_tag("tree.html", name="draw_menu")
def tree_menu(menu: str):
    members = get_members(Menu.objects.get(name=menu))
    return {
        "members": members,
    }
