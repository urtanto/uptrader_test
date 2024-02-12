from django import template

register = template.Library()


def get_list_urls(menu: dict) -> list:
    res = []
    for item in menu["members"]:
        if item["is_url"]:
            res.append(item["url"])
        else:
            res.extend(get_list_urls(item))
    return res


def contains(menu: dict, path: str) -> str:
    return "yes" if path in get_list_urls(menu) else "no"


register.filter("contains", contains)
