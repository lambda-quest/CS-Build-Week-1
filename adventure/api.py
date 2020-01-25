from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
from util.our_world import World 
from django.forms.models import model_to_dict

# AUTH
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

class CreateWorld(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Delete Current Rooms
        Room.objects.all().delete()

        # Make World
        w = World()
        w.createBoard(10,10)
        w.populateWorld()

        # Response
        response = {"Status": 200}
        return JsonResponse(response)

# @csrf_exempt
# @api_view(["GET"])
# def createWorld(request):
    # # Delete Current Rooms
    # Room.objects.all().delete()

    # # Make World
    # w = World()
    # w.createBoard(10,10)
    # w.populateWorld()

    # # Response
    # response = {"Status": 200}
    # return JsonResponse(response)

class GetRooms(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        rooms = Room.objects.all()

        response = []
        for item in rooms:
            item = model_to_dict(item)
            response.append(item)

        return JsonResponse(response, safe=False)
        # return Response(rooms)


# @csrf_exempt
# @api_view(["GET"])
# def getRooms(request):
#     rooms = Room.objects.all()

#     response = []
#     for item in rooms:
#         item = model_to_dict(item)
#         response.append(item)

#     return JsonResponse(response, safe=False)
#     # return Response(rooms)

class Initialize(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        print(f'USER: {user}')
        player = user.player
        print(f'PLAYER: {player}')
        player_id = player.id
        print(f'player_ID {player_id}')
        uuid = player.uuid
        print(f'UUID {uuid}')

        # ERROR
        room = player.room()
        print(f'UUID {uuid}')

        return JsonResponse({'uuid': uuid, 'name':player.user.username, 'id':room.id}, safe=True)



# @csrf_exempt
# @api_view(["GET"])
# def initialize(request):
#     user = request.user
#     print(f'USER: {user}')
#     player = user.player
#     print(f'PLAYER: {player}')
#     player_id = player.id
#     print(f'player_ID {player_id}')
#     uuid = player.uuid
#     print(f'UUID {uuid}')

#     # ERROR
#     room = player.room()

#     # players = room.playerNames(player_id)
#     # return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)
#     return JsonResponse({'uuid': uuid, 'name':player.user.username, 'id':room.id}, safe=True)
    

class Move(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(f'Req.Body: {request.body}')

        # dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
        # reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
        
        player = request.user.player
        # player_id = player.id
        # player_uuid = player.uuid

        data = json.loads(request.body)
        direction = data['direction']

        room = player.room()

        nextRoomID = None
        if direction == "n":
            nextRoomID = room.n_to
        elif direction == "s":
            nextRoomID = room.s_to
        elif direction == "e":
            nextRoomID = room.e_to
        elif direction == "w":
            nextRoomID = room.w_to

        print(f'NEXT ROOM: {nextRoomID}')

        print(nextRoomID is not None)
        print(nextRoomID > 0)
        if nextRoomID is not None and nextRoomID > 0:
            nextRoom = Room.objects.get( id = nextRoomID )

            player.currentRoom = nextRoomID
            player.save()
            
            # players = nextRoom.playerNames(player_id)
            # currentPlayerUUIDs = room.playerUUIDs(player_id)
            # nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)

            # for p_uuid in currentPlayerUUIDs:
            #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
            # for p_uuid in nextPlayerUUIDs:
            #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
            # return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
            
            # return JsonResponse({'name':player.user.username, 'nextRoomID': player.user.currentRoom 'error_msg':""}, safe=True)
            
            
            # return JsonResponse({'name':player.username, 'nextRoomID': player.currentRoom, 'error_msg':""}, safe=True)
            # Response
            response = {"Message": "AWAY WE GO"}
            return JsonResponse(response)
        else:
            # players = room.playerNames(player_id)
            return JsonResponse({'name':player.user.username, 'error_msg':"You cannot move that way."}, safe=True)

# @csrf_exempt
# @api_view(["POST"])
# def move(request):
    # print(f'Req.Body: {request.body}')

    # dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    # reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    # player = request.user.player
    # player_id = player.id
    # player_uuid = player.uuid
    # data = json.loads(request.body)
    # direction = data['direction']
    # room = player.room()
    # nextRoomID = None
    # if direction == "n":
    #     nextRoomID = room.n_to
    # elif direction == "s":
    #     nextRoomID = room.s_to
    # elif direction == "e":
    #     nextRoomID = room.e_to
    # elif direction == "w":
    #     nextRoomID = room.w_to
    # if nextRoomID is not None and nextRoomID > 0:
    #     nextRoom = Room.objects.get(id=nextRoomID)
    #     player.currentRoom=nextRoomID
    #     player.save()
    #     players = nextRoom.playerNames(player_id)
    #     currentPlayerUUIDs = room.playerUUIDs(player_id)
    #     nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
    #     # for p_uuid in currentPlayerUUIDs:
    #     #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
    #     # for p_uuid in nextPlayerUUIDs:
    #     #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
    #     return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    # else:
    #     players = room.playerNames(player_id)
    #     return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


class GetPlayers(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self,request):
        players = Player.objects.all()

        response = []
        for item in players:
            item = model_to_dict(item)
            response.append(item)

        return JsonResponse(response, safe=False)
        # return Response(rooms)


class GetPlayer_by_ID(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        player = request.user.player
        print(player)

        player = Player.objects.get( id=player.id )

        response = model_to_dict(player)

        return JsonResponse(response)













class Say(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)

# @csrf_exempt
# @api_view(["POST"])
# def say(request):
#     # IMPLEMENT
#     return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)