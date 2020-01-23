from adventure.models import Room

# class Room:
#     def __init__(self, id, title, x, y):
#         self.id = id
#         self.title = title
#         # -- #
#         self.x = x
#         self.y = y
#         # -- #
#         self.n_to = None
#         self.s_to = None
#         self.e_to = None
#         self.w_to = None
#         # -- #
#         # self.playerList = []

#     def availableMoves(self, world):
#         moves = {
#             "n_to": True,
#             "s_to": True,
#             "e_to": True,
#             "w_to": True
#         }

#         # Check Y
#         if self.y + 1 >= world.height:
#             moves["n_to"] = False
#         if self.y - 1 < 0:
#             moves["s_to"] = False

#         # Check X
#         if self.x + 1 >= world.width:
#             moves["e_to"] = False
#         if self.x - 1 < 0:
#             moves["w_to"] = False

#         return moves

#     def __str__(self):
#         output = f'id: {self.id} \n'
#         output += f'title: {self.title} \n'
#         output += f'(X, Y) = ({self.x}, {self.y})'

#         return output

class World: 
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def createBoard(self, new_width, new_height):
        # Reset Height * Width
        self.width = new_width
        self.height = new_height

        # Create Empty Board
        board = [None] * new_height
        for row in range( len(board) ):
            board[row] = [None] * new_width
        
        # Save Board to the World's Data attribute
        self.data = board

    def configureRoom(self):
        pass

    def generateRoom(self, title, x, y):
        room = Room(title=title, x=x, y=y)
        room.save()
        
        # print(room)
        # return room

    def populateWorld(self):
        roomCounter = 0
        x_counter = 0
        y_counter = 0

        for row_index in range( self.width ):
            for column_index in range( self.height ):
                # Data Check
                # print(f'PRE: {self.data[row_index][column_index]}')

                # Dynamically configure rooms
                    # Pro / Con Event
                    # Plan Connections?

                # Make Room
                # newRoom = self.generateRoom(roomCounter, 'newRoom', x_counter, y_counter)
                # newRoom = self.generateRoom(roomCounter, x_counter, y_counter)
                self.generateRoom(roomCounter, x_counter, y_counter)
                
                # Save Room
                # self.data[row_index][column_index] = newRoom

                # Data Check
                # print(f'POST: {self.data[row_index][column_index]}')

                # Increment Counters
                roomCounter += 1
                if x_counter >= self.width - 1:
                    x_counter = 0
                    y_counter += 1
                else:
                    x_counter += 1
                    
    # def __str__(self):
    def printWorld(self):
        pass
        # output = f''
        # for row in range( len(self.data) ):
        #     output += f'['
        #     for data in self.data[row]:
        #         # print(f'DATA: {data}')
        #         # output += f'{data.id}@({data.x},{data.y}) // '
        #         output += f'({data.x},{data.y}) // '
        #     output += f']\n'
        # # print(output)
        # return output

     
w = World()
w.createBoard(10,10)
w.populateWorld()

# THIS PRINTS UPSIDOWN!!
# print(w.printWorld())

# print(w.data[0][0].availableMoves(w))
# print(w.data[9][9].availableMoves(w))