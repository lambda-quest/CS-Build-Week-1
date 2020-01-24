from django.conf.urls import url
from . import api

urlpatterns = [
    # url('init', api.initialize),

    # PROTECTED
    url('init', api.Initialize.as_view(), name='init'),
    url('createWorld', api.CreateWorld.as_view(), name='createWorld'), # only needs to be run once on the live server
    url('getRooms', api.GetRooms.as_view(), name='getRooms'),
    url('move', api.Move.as_view(), name='move'),
    url('say', api.Say.as_view(), name='say'),
]