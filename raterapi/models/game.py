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
  
  @property 
  def average_rating(self):
    """average rating for each game"""
    ratings = self.ratings.all()
    
    total_rating = 0
    for rating in ratings:
      total_rating += rating.rating
      
    if len(ratings):
      average_rating = total_rating/len(ratings)
      return average_rating
