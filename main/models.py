from django.db import models


class Menu(models.Model):
    """
    Класс меню

    :param name: название меню которое указывается в html и будет указываться на фронте в списке
    :param parent: привязка либо на самого себя либо на другое меню, из-за чего текущее становится вложенным
    """
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class Url(models.Model):
    """
    Класс url, привязывается url к какому-то меню (Menu)

    :param name: название которого будет отображаться в меню
    :param name_url: либо named url, либо url от корня
    :param parent: привязка к таблице
    """
    name = models.CharField(max_length=255, default="test")
    name_url = models.CharField(max_length=511)
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE)
