from django.db import models

class Discard(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    