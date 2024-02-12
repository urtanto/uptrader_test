from django import template
from main.models import *

register = template.Library()


@register.inclusion_tag("tree.html", name="draw_menu")
def tree_menu(url: str):
    return {}
