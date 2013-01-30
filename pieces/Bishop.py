from Move import Move
import Piece

class Bishop(Piece.Piece):

    def __init__(self, c):
        self.color = c
        
    def get_available_moves(self, matrix, px, py):
        posX = px
        posY = py
        available = list()

        for i in range(1, 7 - posX):
            if posY + i <= 7:
                if matrix[posX + i][posY + i] == None or not matrix[posX + i][posY + i].color == self.color:
                    available.append(Move(posX, posY, posX + i, posY + i))
                if not matrix[posX + i][posY + i] == None:
                    break
        for i in range(1, 7 - posX):
            if posY - i >= 0:
                if matrix[posX + i][posY -i] == None or not matrix[posX + i][posY - i].color == self.color:
                    available.append(Move(posX, posY, posX + i, posY - i))
                if not matrix[posX + i][posY - i] == None:
                    break
        for i in range(1, posX):
            if posY + i <= 7:
                if matrix[posX - i][posY + i] == None or not matrix[posX - i][posY + i].color == self.color:
                    available.append(Move(posX, posY, posX - i, posY + i))
                if not matrix[posX - i][posY + i] == None:
                    break
        for i in range(1, posX):
            if posY - i >= 0:   
                if matrix[posX - i][posY - i] == None or not matrix[posX - i][posY - i].color == self.color:
                    available.append(Move(posX, posY, posX - i, posY - i))
                if not matrix[posX - i][posY - i] == None:
                    break

        return available

    def toString(self):
        if self.color == "W":
            return "BW"
        else: 
            return "BB"


