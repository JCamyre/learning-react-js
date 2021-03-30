from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom

# So the urls for the api app are only for fetching information from database?
urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
]
