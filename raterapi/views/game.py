"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game, Category

class GameView(ViewSet):
  def retrieve(self, request, pk):
    """Handle GET requests for single game"""
    try:
      game = Game.objects.get(pk=pk)
      serializer = GameSerializer(game)
      return Response(serializer.data)
    except Game.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests to get all games"""
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)
    
  def create(self, request):
    """Handle POST requests to create a new game"""
    category_id = Category.objects.get(pk=request.data["category_id"])
    game = Game.objects.create(
      title=request.data["title"],
      description=request.data["description"],
      designer=request.data["designer"],
      year_released=request.data["year_released"],
      number_of_players=request.data["number_of_players"],
      play_time=request.data["play_time"],
      age_rec=request.data["age_rec"],
      category_id=category_id
    )
    serializer = GameSerializer(game)
    return Response(serializer.data)
  
  def update(self, request, pk):
    """Handles PUT requests for updating a game"""
    game = Game.objects.get(pk=pk)
    category_id = Category.objects.get(pk=request.data["category_id"])
    game.title = request.data["title"]
    game.description = request.data["description"]
    game.designer = request.data["designer"]
    game.year_released = request.data["year_released"]
    game.number_of_players = request.data["number_of_players"]
    game.play_time = request.data["play_time"]
    game.age_rec = request.data["age_rec"]
    game.category_id = category_id
    game.save()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'description', 'title', 'designer', 'year_released', 'number_of_players', 'play_time', 'age_rec', 'category_id')
    depth = 2
