from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('createWorld', api.createWorld),
    url('move', api.move),
    url('say', api.say),
]