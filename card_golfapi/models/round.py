from django.db import models

class Round(models.Model):
    open = models.BooleanField()
    name = models.IntegerField()
    game = models.ForeignKey('Game', related_name='Round', on_delete=models.CASCADE)