from django import template
from main.models import *

register = template.Library()

@register.inclusion_tag("", name="")
def tree_menu():
    pass
