from rest_framework import serializers
from .models import Room

# Use serializer for handling requests (either accepting data or outputting)
# I think of serializers as translating a post/get request into Python code

class RoomSerializer(serializers.ModelSerializer): # Converts to database
    class Meta: 
        model = Room 
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at') # the 'id' is the pk (primary key), automatic

# Make sure payload values are valid and fits with model fields. payload = {'votes_to_skip': 3, 'guest_can_pause': False}
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip') # Just put the fields you want to be accepted from post request

