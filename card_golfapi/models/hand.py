from django.db import models
from django.contrib.auth.models import User

class Hand(models.Model):
    player = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    score = models.IntegerField()