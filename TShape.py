# 4 rotation types

class TShape:
    ROTATIONS = [[[0,1,0],
                  [1,1,1],
                  [0,0,0]],#ROTATIONS[0]
                 [[0,1,0],
                  [0,1,1],#ROTATIONS[1]
                  [0,1,0]],
                 [[0,0,0],
                  [1,1,1],
                  [0,1,0]],#ROTATIONS[2]
                 [[0,1,0],
                  [1,1,0],
                  [0,1,0]]]#ROTATIONS[3]  ## Change these to three by three boxes
                                            ## make sure to validate different lines depending on diff shapes and rotations

    
    def __init__(self):
        self.rotation = 0
        self.shape = TShape.ROTATIONS[0]
        self.type = 'T'

    def rotate(self):
        self.rotation += 1
        self.rotation %= 4
        self.updateRotation()

    def updateRotation(self):
        self.shape = TShape.ROTATIONS[self.rotation]

    def delete(self, gameBoard):
        if self.rotation == 0:
            gameBoard.board[gameBoard.x][gameBoard.y + 1] = 0
            for i in range(3):
                gameBoard.board[gameBoard.x + 1][gameBoard.y + i] = 0
                
        elif self.rotation == 1:
            for i in range(3):
                gameBoard.board[gameBoard.x + i][gameBoard.y + 1] = 0
            gameBoard.board[gameBoard.x + 1][gameBoard.y + 2] = 0
            
        elif self.rotation == 2:
            for i in range(3):
                gameBoard.board[gameBoard.x + 1][gameBoard.y + i] = 0
            gameBoard.board[gameBoard.x + 2][gameBoard.y + 1] = 0
            
        else:
            for i in range(3):
                gameBoard.board[gameBoard.x + i][gameBoard.y + 1] = 0
            gameBoard.board[gameBoard.x + 1][gameBoard.y] = 0

    def collideRight(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret =  gb[x][y + 2] or gb[x + 1][y + 3]
                
        elif self.rotation == 1:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret = gb[x][y + 2] or gb[x + 1][y + 3] or gb[x + 2][y + 2]
                
        elif self.rotation == 2:
            if y == gameBoard.COLS - 3:
                ret = True
            else:
                ret = gb[x + 2][y + 2] or gb[x + 1][y + 3]
                
        else:
            if y == gameBoard.COLS - 2:
                ret = True
            else:
                ret = gb[x][y + 2] or gb[x + 1][y + 2] or gb[x + 2][y + 2]
                
        return ret

    def collideLeft(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if y == 0:
                ret = True
            else:
                ret =  gb[x][y] or gb[x + 1][y - 1]
                
        elif self.rotation == 1:
            if y == -1:
                ret = True
            else:
                ret = gb[x][y] or gb[x + 1][y] or gb[x + 2][y]
                
        elif self.rotation == 2:
            if y == 0:
                ret = True
            else:
                ret = gb[x + 1][y - 1] or gb[x + 2][y]
                
        else:
            if y == 0:
                ret = True
            else:
                ret = gb[x][y] or gb[x + 1][y - 1] or gb[x + 2][y]
                
        return ret

    def collideDown(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = False
        if self.rotation == 0:
            if x == gameBoard.ROWS - 2:
                ret = True
            else:
                ret =  gb[x + 2][y] or gb[x + 2][y + 1] or gb[x + 2][y + 2]
                
        elif self.rotation == 1:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 3][y + 1] or gb[x + 2][y + 2]
                
        elif self.rotation == 2:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 2][y] or gb[x + 3][y + 1] or gb[x + 2][y + 2]
                
        else:
            if x == gameBoard.ROWS - 3:
                ret = True
            else:
                ret = gb[x + 2][y] or gb[x + 3][y + 1]
                
        return ret
        
    def canRotate(self, gameBoard):
        x = gameBoard.x
        y = gameBoard.y
        gb = gameBoard.board
        ret = True
        if self.rotation == 0:
            if x == gameBoard.ROWS - 2:
                ret = False
            else:
                ret = not gb[x + 2][y + 1]
                
        elif self.rotation == 1:
            if y == -1:
                ret = False
            else:
                ret = not gb[x + 1][y]
                
        elif self.rotation == 2:
            ret = not gb[x][y + 1]
            
        else:
            if y != gameBoard.COLS - 2:
                ret = not gb[x + 1][y + 2]
            else:
                ret = False
                
        return ret
    
