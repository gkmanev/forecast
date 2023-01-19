from django.db import models
from datetime import datetime

class OverTwoAndHalf(models.Model):
    homeTeam = models.CharField(max_length=400)
    awayTeam = models.CharField(max_length=400)    
    startTime = models.DateTimeField(default=datetime.now())
    home_over_percentage = models.IntegerField()
    away_over_percentage = models.IntegerField()
    championship = models.CharField(max_length=400)
    bet_url = models.CharField(max_length=600, null=True)