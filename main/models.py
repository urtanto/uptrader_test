from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class Url(models.Model):
    name = models.CharField(max_length=255, default="test")
    name_url = models.CharField(max_length=511, unique=True)
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE)
