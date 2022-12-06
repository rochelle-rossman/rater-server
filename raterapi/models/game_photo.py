from django.db import models
from .game import Game
from .player import Player

class GamePhoto(models.Model):
  game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
  player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
  url = models.ImageField(upload_to='images')
