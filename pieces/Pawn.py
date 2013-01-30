import Piece
import copy
from Move import Move

class Pawn(Piece.Piece):

    def __init__(self, c):
        self.color = c
        self.first_move = 1
   
    def get_available_moves(self, matrix, px, py):
        posX = px
        posY = py
        available = list()
        if self.color == "B":
            if matrix[posX - 1][posY] == None:
                available.append(Move(posX, posY, posX - 1, posY))
                if self.first_move and matrix[posX - 2][posY] == None:
                    available.append(Move(posX, posY, posX - 2, posY))
            if posY < 7 and (not matrix[posX - 1][posY + 1] == None and matrix[posX - 1][posY + 1].color == "W"):
                available.append(Move(posX, posY, posX - 1, posY + 1))
            if posY > 0 and (not matrix[posX - 1][posY - 1] == None and matrix[posX - 1][posY - 1].color == "W"):
                available.append(Move(posX, posY, posX - 1, posY - 1))
        else:
            if matrix[posX + 1][posY] == None:
                available.append(Move(posX, posY, posX + 1, posY))
                if self.first_move and matrix[posX + 2][posY] == None:
                    available.append(Move(posX, posY, posX + 2, posY))
            if posY < 7 and (not matrix[posX + 1][posY + 1] == None and matrix[posX + 1][posY + 1].color == "B"):
                available.append(Move(posX, posY, posX + 1, posY + 1))
            if posY > 0 and (not matrix[posX + 1][posY - 1] == None and matrix[posX + 1][posY - 1].color == "B"):
                available.append(Move(posX, posY, posX + 1, posY - 1))
        return available          

    def toString(self):
        if self.color == "W":
            return "PW"
        else: 
            return "PB"
    


