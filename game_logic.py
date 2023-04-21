import random

class App2048:
    def __init__(self): #initializing board
        self.board = [[0] * 4, [0] * 4, [0] * 4,  [0] * 4] 

    def preGameSetUp(self):
        #creates the 2 random '2's for the start of the game
        i = 0
        while i < 2:
            x = random.randrange(0,4)
            y = random.randrange(0,4)
            if self.board[y][x] == 0:
                self.board[y][x] = 2
                i += 1
            else:
                continue

    def __repr__(self):
        string = f'''{self.board[0][0]} {self.board[0][1]} {self.board[0][2]} {self.board[0][3]}
{self.board[1][0]} {self.board[1][1]} {self.board[1][2]} {self.board[1][3]} 
{self.board[2][0]} {self.board[2][1]} {self.board[2][2]} {self.board[2][3]}
{self.board[3][0]} {self.board[3][1]} {self.board[3][2]} {self.board[3][3]}
'''
        return string

    def define(self, b):
        self.board = b
    

    def pickTwoOrFour(self):
        '''This function will automatically generate 
        a 2 or a 4 after a move is made'''
        assigned = False
        while not assigned:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
            if self.board[y][x] == 0:
                self.board[y][x] = random.choice((2, 4))
                assigned = True

    def upMove(self):
        '''this function will move up'''
        for x in range(0, 4):
            shift = 0
            for y in range(0, 4):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y - shift][x] = self.board[y][x]
                    self.board[y][x] = 0
        for x in range(0, 4):
            for y in range(0, 4):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y + 1][x]:
                    self.board[y][x] *= 2
                    self.board[y + 1][x] = 0

    def downMove(self):   
        '''this function will move down'''
        for x in range(0, 4):
            shift = 0
            for y in range(3, -1, -1):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y + shift][x] = self.board[y][x]
                    self.board[y][x] = 0
        for x in range(0, 4):
            for y in range(3, 0, -1):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y - 1][x]:
                    self.board[y][x] *= 2
                    self.board[y - 1][x] = 0
    
    def leftMove(self):
        '''this function will move left'''
        for y in range(0, 4):
            shift = 0
            for x in range(0, 4):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y][x - shift] = self.board[y][x]
                    self.board[y][x] = 0
        for y in range(0, 4):
            for x in range(0, 4):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x + 1]:
                    self.board[y][x] *= 2
                    self.board[y][x + 1] = 0

    def rightMove(self):
        '''this function goes right'''
        for y in range(0, 4):
            shift = 0
            for x in range(3, -1, -1):
                if self.board[y][x] == 0:
                    shift += 1
                elif shift == 0:
                    continue
                else:
                    self.board[y][x + shift] = self.board[y][x]
                    self.board[y][x] = 0
        for y in range(0, 4):
            for x in range(3, 0, -1):
                if self.board[y][x] != 0 and self.board[y][x] == self.board[y][x - 1]:
                    self.board[y][x] *= 2
                    self.board[y][x - 1] = 0
    
    def fullUp(self):
        self.upMove()
        self.upMove()
        self.upMove()
        self.upMove()
        self.upMove()
        self.pickTwoOrFour()
    
    def fullDown(self):
        self.downMove()
        self.downMove()
        self.downMove()
        self.downMove()
        self.downMove()
        self.pickTwoOrFour()
    
    def fullLeft(self):
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.leftMove()
        self.pickTwoOrFour()
    
    def fullRight(self):
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.rightMove()
        self.pickTwoOrFour()
                
'''game1 = App2048()
game1.preGameSetUp()
print(f'pregame set up: \n{game1}')
game1.upMove()
print(f'up move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.downMove()
print(f'down move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.leftMove()
print(f'left move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.downMove()
print(f'down move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.upMove()
print(f'up move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')
game1.rightMove()
print(f'right move: \n{game1}')
game1.pickTwoOrFour()
print(f'pick two or four: \n{game1}')'''

'''game = App2048()
game.define([[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]])
print(game)
game.fullUp()
print(game)
game.define([[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]])
game.fullDown()
print(game)
game.define([[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]])
game.fullLeft()
print(game)
game.define([[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]])
game.fullRight()
print(game)'''

'''game = App2048()
game.preGameSetUp()
print(game)
game.fullUp()
print(game)
game.fullDown()
print(game)
game.fullLeft()
print(game)
game.fullRight()
print(game)
game.fullUp()
print(game)
game.fullDown()
print(game)
game.fullLeft()
print(game)
game.fullRight()
print(game)'''