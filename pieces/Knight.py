import Piece
from Move import Move

class Knight(Piece.Piece):

    def __init__(self, c):
        self.color = c

    def get_available_moves(self, matrix, px, py):
        posX = px
        posY = py
        available = list()
        if posX - 1 >= 0:
            if posY - 2 >= 0:
                if matrix[posX - 1][posY - 2] == None or not matrix[posX - 1][posY - 2].color == self.color:
                    available.append(Move(posX, posY, posX - 1, posY - 2))        
            if posY + 2 <= 7:
                if matrix[posX - 1][posY + 2] == None or not matrix[posX - 1][posY + 2].color == self.color:
                    available.append(Move(posX, posY, posX - 1, posY + 2))

        if posX - 2 >= 0:
            if posY - 1 >= 0:
                if matrix[posX - 2][posY + 1] == None or not matrix[posX - 2][posY + 1].color == self.color:
                    available.append(Move(posX, posY, posX - 2, posY + 1))
            if posY + 1 <= 7:
                if matrix[posX - 2][posY + 1] == None or not matrix[posX - 2][posY + 1].color == self.color:
                    available.append(Move(posX, posY, posX - 2, posY + 1))

        if posX + 1 <= 7:
            if posY - 2 >= 0:
                if matrix[posX + 1][posY - 2] == None or not matrix[posX + 1][posY - 2].color == self.color:
                    available.append(Move(posX, posY, posX + 1, posY - 2))

            if posY + 2 <= 7:
                if matrix[posX + 1][posY + 2] == None or not matrix[posX + 1][posY + 2].color == self.color:
                    available.append(Move(posX, posY, posX + 1, posY + 2))

        if posX + 2 <= 7:
            if posY - 1 >= 0:
                if matrix[posX + 2][posY - 1] == None or not matrix[posX + 2][posY - 1].color == self.color:
                    available.append(Move(posX, posY, posX + 2, posY - 1))

            if posY + 1 <= 7:
                if matrix[posX + 2][posY + 1] == None or not matrix[posX + 2][posY + 1].color == self.color:
                    available.append(Move(posX, posY, posX + 2, posY + 1))

        return available


    def toString(self):
        if self.color == "W":
            return "RW"
        else: 
            return "RB"






