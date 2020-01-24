from django.conf.urls import url
from . import api

urlpatterns = [
    # PROTECTED
    url('createWorld', api.CreateWorld.as_view(), name='createWorld'), # only needs to be run once on the live server
    
    url('init', api.Initialize.as_view(), name='init'),
    url('getRooms', api.GetRooms.as_view(), name='getRooms'),
    url('getPlayers', api.GetPlayers.as_view(), name='getPlayers'),
    url('getPlayer', api.GetPlayer_by_ID.as_view(), name='getPlayer'),
    url('move', api.Move.as_view(), name='move'),

    url('say', api.Say.as_view(), name='say'),
]