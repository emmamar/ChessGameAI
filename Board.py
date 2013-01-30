from pieces import Castle
from pieces import King
from pieces import Queen
from pieces import Bishop
from pieces import Knight
from pieces import Pawn

class Board:
    def __init__ (self, f):       
        '''create matrix from file'''
        self.matrix = list()
                                     
        i = 0
        for line in f:              
            row_list = str.split(line)
            self.matrix.append(list())
            for item in row_list:
		self.matrix[i].append(self.createPiece(item)) 
            i += 1
        print self.toString()

    def createPiece(self, item):
        if item[1:2] == "B":
            if item[0:1] == "P":
                return Pawn.Pawn("B") 
            elif item[0:1] == "K": 
                return King.King("B") 
            elif item[0:1] == "Q": 
                return Queen.Queen("B") 
            elif item[0:1] == "B":
                return Bishop.Bishop("B")
            elif item[0:1] == "R": 
                return Knight.Knight("B") 
            elif item[0:1] == "C": 
                return Castle.Castle("B")
        elif item[1:2] == "W":
            if item[0:1] == "P": 
                return Pawn.Pawn("W") 
            elif item[0:1] == "K": 
                return King.King("W") 
            elif item[0:1] == "Q": 
                return Queen.Queen("W") 
            elif item[0:1] == "B": 
                return Bishop.Bishop("W")
            elif item[0:1] == "R": 
                return Knight.Knight("W") 
            elif item[0:1] == "C": 
                return Castle.Castle("W")  

    def movePiece(self, move):
        self.matrix[move.endX][move.endY] = self.matrix[move.startX][move.startY]
        self.matrix[move.startX][move.startY] = None
        f = open('Board.txt', 'w')
        f.write(self.toString())

    def getMatrix(self):
        return matrix
    
    def getValueAt(self,x,y):
        if (x < 0 or x >= 8 or y < 0 or y >= 8):
            print "not in range"
        return matrix[x][y].toString()
    
    def toString(self):
        board_string = ''
        for i in range(0,8): 
            for j in range(0,8):
                if self.matrix[i][j] == None:
                    board_string += "00" + ' '
                else:
                    board_string += self.matrix[i][j].toString() + ' '
            board_string += '\n'
        return board_string

    def is_check_mate(self):
        return True


