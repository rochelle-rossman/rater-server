from django.db import models
from .player import Player
from .game import Game

class Review(models.Model):
  player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
  game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
  comment = models.CharField(max_length=500)
