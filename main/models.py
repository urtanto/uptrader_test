from django.db import models


class RootUrl(models.Model):
    url = models.CharField(max_length=255)


class ChildUrl(models.Model):
    url = models.CharField(max_length=255)
    parent = models.ForeignKey(RootUrl, on_delete=models.CASCADE)
