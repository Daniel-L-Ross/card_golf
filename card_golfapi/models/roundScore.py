from django.db import models
from django.contrib.auth.models import User

class RoundScore(models.Model):
    round = models.ForeignKey("Round", on_delete=models.DO_NOTHING)
    player = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    score = models.IntegerField()