from django.db import models

class Deck(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    