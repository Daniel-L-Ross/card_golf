from django.db import models

class DeckCard(models.Model):
    deck = models.ForeignKey("Deck", on_delete=models.CASCADE)
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    