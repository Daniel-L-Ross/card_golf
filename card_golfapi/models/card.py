from django.db import models

class Card(models.Model):
    suite = models.CharField()
    name = models.CharField()
    score = models.IntegerField()
    image = models.URLField()