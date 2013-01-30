import Piece
import copy
from Move import Move

class King(Piece.Piece):

    def __init__(self, c):
        self.color = c

    def get_available_moves(self, matrix, px, py):
        posX = px
        posY = py
        available = list()
        if posX < 7:
            if matrix[posX + 1][posY] == None or not matrix[posX + 1][posY].color == self.color:
                available.append(Move(posX, posY, posX + 1, posY))
        if posX > 0:
            if matrix[posX - 1][posY] == None or not matrix[posX - 1][posY].color == self.color:
                available.append(Move(posX, posY, posX - 1, posY))
        if posY < 7:
            if matrix[posX][posY + 1] == None or not matrix[posX][posY + 1].color == self.color:
                available.append(Move(posX, posY, posX, posY + 1))
        if posY > 0:
            if matrix[posX][posY - 1] == None or not matrix[posX][posY - 1].color == self.color:
                available.append(Move(posX, posY, posX, posY - 1))
        return available
        
    def toString(self):
        if self.color == "W":
            return "KW"
        else: 
            return "KB"
