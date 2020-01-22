# IMPORTS
# from adventure.models import Player, Room

#PASTA 
class Room:
    # def __init__(self, id, title, description, x, y):
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None
        # self.x = x
        # self.y = y

Class World: 
    pass

# Notes:
# World = 2d Array
    # know the fixed size of world => 10 x 10

# Iterate through world 
    # for each empty room assign index

# In memory 2d array 



# Steos:
# 1 - Create Chess Board
def createWorld(x, y):
    world = [None] * y

    for i in range( len(world) ):
        world[i] = [None] * x

    # print(world)
    return world

def create_realRoom(num):
    room = Room(
        title=f'Room Num:{num}', description="Generic", id=num
    )
    return room

def populate_world():
    created_world = createWorld(10,10)
    counter = 0

    for row in created_world:
        for column in row:
            print(f'PRE: {column}')
            # column = create_realRoom(counter)
            column = 'TACO JOHNSON'
            print(f'POST: {column}')
            # print(column.id)
            
            counter += 1
    return created_world


FINAL_output = populate_world()
print(FINAL_output)





