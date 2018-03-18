from django.db import models
from jsonfield import JSONField


class TheGame(models.Model):
    game_data = JSONField()
