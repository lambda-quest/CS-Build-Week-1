from django.conf.urls import url
from . import api
from rest_framework import routers
from .api import RoomViewSet

<<<<<<< HEAD
# urlpatterns = [
#     url('init', api.initialize),
#     url('move', api.move),
#     url('say', api.say),
# ]

router = routers.DefaultRouter()
router.register('', RoomViewSet, 'rooms')

urlpatterns = router.urls
=======
urlpatterns = [
    url('init', api.initialize),
    url('createWorld', api.createWorld), # only needs to be run once on the live server
    url('getRooms', api.getRooms),
    url('move', api.move),
    url('say', api.say),
]
>>>>>>> e502bd3260fc90b3e1fe9823154527611083423d
