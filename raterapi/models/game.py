from django.db import models

class Game(models.Model):
  description = models.CharField(max_length=800)
  title = models.CharField(max_length=100)
  designer = models.CharField(max_length=100)
  year_released = models.DateField()
  number_of_players = models.IntegerField()
  play_time = models.TimeField()
  age_rec = models.IntegerField()
