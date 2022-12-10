from django.db import models
from .category import Category

class Game(models.Model):
  description = models.CharField(max_length=800)
  title = models.CharField(max_length=100)
  designer = models.CharField(max_length=100)
  year_released = models.DateField()
  number_of_players = models.IntegerField()
  play_time = models.TimeField()
  age_rec = models.IntegerField()
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
