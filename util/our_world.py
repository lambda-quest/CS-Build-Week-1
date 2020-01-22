# IMPORTS
# from adventure.models import Player, Room

# PASTA


class Player:
    def __init__(self, world):
        self.current_room = world[0][0]
        self.world = world

    def move_player(self, movement_key):
        if movement_key == "n":
            self.check_bounds(movement_key)
            self.current_room = self.world[self.current_room.x][self.current_room.y + 1]
        if movement_key == "e":
            self.check_bounds(movement_key)
            self.current_room = self.world[self.current_room.x +
                                           1][self.current_room.y]
        if movement_key == "s":
            self.check_bounds(movement_key)
            self.current_room = self.world[self.current_room.x][self.current_room.y - 1]
        if movement_key == "w":
            self.check_bounds(movement_key)
            self.current_room = self.world[self.current_room.x -
                                           1][self.current_room.y]

    def check_bounds(self, movement_key):
        if movement_key == "n":
            if self.current_room.y < len(self.world)-1:
                pass
            else:
                return "You cannot move up a level."
        if movement_key == "e":
            if self.current_room.x < len(self.world[0])-1:
                pass
            else:
                return "You cannot move to the right."
        if movement_key == "s":
            if self.current_room.y > 0:
                pass
            else:
                return "You cannot move down a level."
        if movement_key == "w":
            if self.current_room.x > 0:
                pass
            else:
                return "You cannot move to the left."


class Room:
    # def __init__(self, id, title, description, x, y):
    # def __init__(self, id, title, description):
    def __init__(self, x, y):
        # self.id = id
        # self.title = title
        # self.description = description
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
        self.x = x
        self.y = y

    def __str__(self):
        output = f'X: {self.x}, Y: {self.y}'
        return output


class World:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate_world(self):
        world = [None] * self.y
        for i in range(len(world)):
            world[i] = [None] * self.x
        counter = 0
        for row in world:
            for column in range(len(row)):
                row[column] = Room(row, column)
                counter += 1
        return world


world_instance = World(10, 10)
new_world = world_instance.generate_world()
ronny = Player(new_world)

while(True):
    print("Enter a movement: ")
    x = input()
    ronny.move_player(x)
    print(
        f'You are currently at [{ronny.current_room.x, ronny.current_room.y}]')
