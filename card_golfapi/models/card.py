from django.db import models

class Card(models.Model):
    suite = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    score = models.IntegerField()
    image = models.URLField(blank=True)