from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game, Player, Rating

class RatingView(ViewSet):
  def create(self, request):
    game = Game.objects.get(pk=request.data["game_id"])
    player = Player.objects.get(pk=request.data["player_id"])
    players_rating = Rating.objects.create(
      player_id = player,
      game_id = game,
      rating = request.data["rating"]
    )
    
    serializer = RatingSerializer(players_rating)
    return Response(serializer.data)
    
class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('id', 'player_id', 'rating', 'game_id')
