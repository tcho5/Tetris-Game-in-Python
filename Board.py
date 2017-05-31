from TShape import *
from OShape import *
from SShape import *
from LShape import *
from JShape import *
from ZShape import *
from IShape import *
import random, pygame, sys
from GameOverGui import *

class Board:
    COLS = 10   
    ROWS = 22
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), \
                  random.randint(0, 255))
        self.board = []
        for row in range(Board.ROWS):
            row = []
            for col in range(Board.COLS):
                row.append(0)
            self.board.append(row)

        self.currentShape = JShape()
        self.heldShape = None
        self.x = 0
        self.y = 3
        self.score = 0
        
        self.draw()

    def check(self):
        for row in range(len(self.currentShape.shape)):
            for col in range(len(self.currentShape.shape[row])):
                if self.board[row][col] == True:
                    pygame.quit()
                    GameOverGui(self.score)
 #                   OpenGui.newGame()
                    sys.exit()
                    #Gameover GUI
                    
    def draw(self):
        for row in range(len(self.currentShape.shape)):
            for col in range(len(self.currentShape.shape[row])):
                if self.currentShape.shape[row][col]:
                    self.board[self.x + row][self.y + col] = \
                                      self.currentShape.shape[row][col]

    def left(self):
        if not self.currentShape.collideLeft(self):
            self.currentShape.delete(self)    
            self.y -= 1
            self.draw()

    def right(self):
        if not self.currentShape.collideRight(self):
            self.currentShape.delete(self)
            self.y += 1
            self.draw() 

    def down(self):
        if not self.currentShape.collideDown(self):
            self.currentShape.delete(self)
            self.x += 1
            self.draw()
        else:
            self.lineClear()
            self.x = 0
            self.y = 2
            self.randomShape()
            self.color = (random.randint(0,255), \
                          random.randint(0, 255), random.randint(0, 255))
            self.check()
            self.draw()

    def up(self):
        if self.currentShape.canRotate(self):
            self.currentShape.delete(self)
            self.currentShape.rotate()
            self.draw()
            
    def lineClear(self):
        for i, row in enumerate(self.board):
            if all(row):
                self.board.pop(i)
                self.score += 10
                newRow = []
                for j in range(Board.COLS):
                    newRow.append(0)

                self.board.insert(0, newRow)
                
    def randomShape(self):
        randNum = random.randint(0, 6)
        if randNum == 0:
            self.currentShape = TShape()
            
        elif randNum == 1:
            self.currentShape = LShape()

        elif randNum == 2:
            self.currentShape = IShape()

        elif randNum == 3:
            self.currentShape = OShape()

        elif randNum == 4:
            self.currentShape = JShape()

        elif randNum == 5:
            self.currentShape = SShape()

        else:
            self.currentShape = ZShape()

    def hardDrop(self):
        while not self.currentShape.collideDown(self):
            self.down()
        self.down()

    def hold(self):
        if not self.heldShape:
            self.heldShape = self.currentShape
            self.currentShape.delete(self)
            self.randomShape()
            self.x = 0
            self.y = 2
            self.draw()
        else:
            tempShape = self.currentShape
            self.currentShape.delete(self)
            self.currentShape = self.heldShape
            self.x = 0
            self.y = 2
            self.draw()
            self.heldShape = tempShape

##    def checkSpawn(self):
##        for i in range(
        

                
        
        
        
        
##            
##def main():
##    tetrisBoard = Board()
##    tetrisBoard.up()
##    tetrisBoard.up()
##    tetrisBoard.up()
##    tetrisBoard.show()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.right()
##    tetrisBoard.up()
##    tetrisBoard.show()
##    

   # for i in range(25):
#        tetrisBoard.up()
#        tetrisBoard.down()
#        print()
#        tetrisBoard.show()

#main()
