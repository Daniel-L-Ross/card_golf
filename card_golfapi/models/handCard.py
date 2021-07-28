from django.db import models

class HandCard(models.Model):
    hand = models.ForeignKey("Hand", on_delete=models.CASCADE)
    card = models.ForeignKey("Card", on_delete=models.CASCADE)
    revealed = models.BooleanField()
    