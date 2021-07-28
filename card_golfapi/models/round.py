from django.db import models

class Round(models.Model):
    open = models.BooleanField()
    name = models.CharField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)