from django.shortcuts import render
from rest_framework import generics, status
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'

    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg) # From the requests GET request, get/retrieve the url's code, which is the room code.
        if code != None:
            room = Room.objects.filter(code=code) # Retrieve room using room code from database
            if len(room) > 0:
                data = RoomSerializer(room[0]).data 
                data['is_host'] = self.request.session.session_key == room[0].host # See if current session_key is equal to that of the host of the room
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid Room Code.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Bad Request': 'Code parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)


class CreateRoomView(APIView): # APIView has very important methods for requests of data from API's
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None): # Handles post requests for this specific view/webpage
        if not self.request.session.exists(self.request.session.session_key): # If host hasn't created a session before or session ran out
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data) # Serialize post data
        if serializer.is_valid(): # Check if post data good 
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host) # Check to see if a room already exists with a host
            if queryset.exists():
                room = queryset[0] # Update the room's information
                room.guest_can_pause = guest_can_pause 
                room.votes_to_skip = votes_to_skip 
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else: 
                room = Room(host=host, guest_can_pause=guest_can_pause, 
                            votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)




