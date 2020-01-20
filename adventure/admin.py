# IMPORTS
from django.contrib import admin

# MODELS
from .models import Player, Room

# Register your models here.
admin.site.register(Player)
admin.site.register(Room)