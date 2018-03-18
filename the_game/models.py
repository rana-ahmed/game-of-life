from django.db import models


class TheGame(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    data = models.CharField(max_length=1000000)
