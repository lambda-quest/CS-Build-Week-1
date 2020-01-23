from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('createWorld', api.createWorld), # only needs to be run once on the live server
    url('getRooms', api.getRooms),
    url('move', api.move),
    url('say', api.say),
]