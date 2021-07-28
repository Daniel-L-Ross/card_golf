from django.db import models

class GameType(models.Model):
    name = models.CharField()
    cardCount = models.IntegerField()
