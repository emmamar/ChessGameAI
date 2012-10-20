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
                self.matrix[i].append(item) 
            i += 1

        '''create list of black and white pieces'''
        self.black_pieces = list()
        self.white_pieces = list() 
        self.createPieces()


    def createPieces(self):
        for i in range(0,8):
            for j in range(0,8):
                if (self.matrix[i][j][1:2] == "B"):
                    if(self.matrix[i][j][0:1] == "P"):
                        self.black_pieces.append(Pawn.Pawn("B", i, j))
                    elif (self.matrix[i][j][0:1] == "K"):
                        self.black_pieces.append(King.King("B", i, j))
                    elif (self.matrix[i][j][0:1] == "Q"):
                        self.black_pieces.append(Queen.Queen("B", i, j))
                    elif (self.matrix[i][j][0:1] == "B"):
                        self.black_pieces.append(Bishop.Bishop("B", i, j))
                    elif (self.matrix[i][j][0:1] == "R"):
                        self.black_pieces.append(Knight.Knight("B", i, j))
                    elif (self.matrix[i][j][0:1] == "C"):
                        self.black_pieces.append(Castle.Castle("B", i, j))
                elif (self.matrix[i][j][1:2] == "W"):
                    if(self.matrix[i][j][0:1] == "P"):
                        self.white_pieces.append(Pawn.Pawn("W", i, j))
                    elif (self.matrix[i][j][0:1] == "K"):
                        self.white_pieces.append(King.King("W", i, j))
                    elif (self.matrix[i][j][0:1] == "Q"):
                        self.white_pieces.append(Queen.Queen("W", i, j))
                    elif (self.matrix[i][j][0:1] == "B"):
                        self.white_pieces.append(Bishop.Bishop("W", i, j))
                    elif (self.matrix[i][j][0:1] == "R"):
                        self.white_pieces.append(Knight.Knight("W", i, j))
                    elif (self.matrix[i][j][0:1] == "C"):
                        self.white_pieces.append(Castle.Castle("W", i, j))
                    

    def movePiece(self, x1, y1, x2, y2):
        pass

    def getMatrix(self):
        return matrix
    
    def getValueAt(self,x,y):
        if (x < 0 or x >= 8 or y < 0 or y >= 8):
            print "not in range"
        return matrix[x][y]
    
    def toString(self):
        board_string = ''
        for i in range(0,8): 
            for j in range(0,8):
                board_string += self.matrix[i][j] + ' '
            board_string += '\n'
        return board_string


    def get_black_pieces(self):
        return self.black_pieces

    def get_white_pieces(self):
        return self.white_pieces

    def get_available_white_moves(self):
        available_moves = list()
        for piece in self.white_pieces:   
             per_piece = piece.get_available_moves(self.matrix)
             for moves in per_piece:
                 available_moves.append(moves)
        for matx in available_moves:
            for line in matx:
                print line
            print "\n"
        return available_moves
             



