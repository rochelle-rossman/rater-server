from django.db import models
from .game import Game
from .category import Category

class GameCategory(models.Model):
  game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="categories")
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
