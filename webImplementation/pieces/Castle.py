import Piece
import copy
from Move import Move

class Castle(Piece.Piece):
    def __init__(self, c):
        self.color = c

    def get_available_moves(self, matrix, px, py):
        posX = px
        posY = py
        available = list()

        for i in range(1,7):
            if posX + i >= 8:
                break
            if matrix[posX + i][posY] == None or not matrix[posX + i][posY].color == self.color:  
                available.append(Move(posX, posY, posX + i, posY))
            if not matrix[posX + i][posY] == None:
                break
        for i in range(1,7):
            if posX - i < 0:
                break
            if matrix[posX - i][posY] == None or not matrix[posX - i][posY].color == self.color:
                available.append(Move(posX, posY, posX - i, posY))
            if not matrix[posX - i][posY] == None:
                break
        for i in range(1,7):
            if posY + i >= 8:
                break
            if matrix[posX][posY + i] == None or not matrix[posX][posY + i].color == self.color:
                available.append(Move(posX, posY, posX, posY + i))
            if not matrix[posX][posY + i] == None:
                break
        for i in range(1,7):
            if posY - i < 0:
                break
            if matrix[posX][posY - i] == None or not matrix[posX][posY - i].color == self.color:
                available.append(Move(posX, posY, posX, posY - i))
            if not matrix[posX][posY - i] == None:
                break
        return available        

    def toString(self):
        if self.color == "W":
            return "CW"
        else: 
            return "CB"
