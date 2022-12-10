from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Review, Game, Player

class ReviewView(ViewSet):
  def list(self, request):
    """Handles GET request for reviews"""
    reviews = Review.objects.all()
    game= request.query_params.get('game', None)
    if game is not None:
      reviews = reviews.filter(reviews=game)
      
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handles PUT request to create a review"""
    game_id = Game.objects.get(pk=request.data["game_id"])
    player_id = Player.objects.get(pk=request.data["player_id"])
    review = Review.objects.create(
      game_id = game_id,
      player_id = player_id,
      comment = request.data["comment"]
    )
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
    
    
class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""
    class Meta:
      model = Review
      fields = ('id', 'game_id', 'player_id', 'comment')
      depth = 1
