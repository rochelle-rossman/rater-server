from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game, Category, GameCategory

class GameCategoryView(ViewSet):
  def list(self, request):
    game_categories = GameCategory.objects.all()
    serializer = GameCategorySerialzer(game_categories, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk):
    try:
      game_category = GameCategory.objects.get(pk=pk)
      serializer = GameCategorySerialzer(game_category)
      return Response(serializer.data)
    except GameCategory.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
  def create(self, request):
    game_id = Game.objects.get(pk=request.data["game_id"])
    category_id = Category.objects.get(pk=request.data["category_id"])
    game_category = GameCategory.objects.create(
      game_id = game_id,
      category_id = category_id
    )
    
    serializer = GameCategorySerialzer(game_category)
    return Response(serializer.data)
  
  def update(self, request, pk):
    pass
    
    
class GameCategorySerialzer(serializers.ModelSerializer):
  class Meta:
    model = GameCategory
    fields = ('id', 'game_id', 'category_id')
    depth = 1
