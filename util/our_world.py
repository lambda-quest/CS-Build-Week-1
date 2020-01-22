# IMPORTS
# from adventure.models import Player, Room

# PASTA


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


class World:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def generate_empty_world(self):
        world = [None] * self.y
        for i in range(len(world)):
            world[i] = [None] * self.x
        counter = 0
        for row in world:
            for i in range(len(row)):
                row[i] = counter
                counter += 1
        return world


world_instance = World(10, 10)
new_world = world_instance.generate_empty_world()
print(new_world)


# def create_realRoom(num):
#     room = Room(
#         title=f'Room Num:{num}', description="Generic", id=num
#     )
#     return room

# def populate_world():
#     created_world = createWorld(10,10)
#     counter = 0

#     for row in created_world:
#         for column in row:
#             print(f'PRE: {column}')
#             # column = create_realRoom(counter)
#             column = 'TACO JOHNSON'
#             print(f'POST: {column}')
#             # print(column.id)

#             counter += 1
#     return created_world


# FINAL_output = populate_world()
# print(FINAL_output)
