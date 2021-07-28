from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Game(models.Model):
    playerCount = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(4)],)
    gameType = models.ForeignKey("GameType", on_delete=models.DO_NOTHING)
    needPlayers = models.BooleanField()
    complete = models.BooleanField()
    playerAction = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    round = models.ForeignKey("Round", on_delete=models.DO_NOTHING)
    winner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
