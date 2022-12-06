from raterapi.models import Player
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Player

    Method arguments:
      request -- The full HTTP request object
    '''
    
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    try:
        player = Player.objects.get(uid=uid)

    # If authentication was successful, respond with their token
        data = {
            'id': player.id,
            'uid': player.uid,
            'bio': player.bio
        }
        return Response(data)
    except:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new player for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the raterapi_player table
    player = Player.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    # Return the player info to the client
    data = {
            'id': player.id,
            'uid': player.uid,
            'bio': player.bio
    }
    return Response(data)
