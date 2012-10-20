import Piece
import copy

class Queen(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.positionX = pX
        self.positionY = pY


    def get_available_moves(self, matrix):
        available = list()
        for i in range(1,7):
            if(self.posX + i >= 8):
                break
            if not(matrix[self.posX + i][self.posY][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX + i, self.posY))
            if not(matrix[self.posX + i][self.posY] == "00"):
                break
        for i in range(1,7):
            if(self.posX - i < 0):
                break
            if not(matrix[self.posX - i][self.posY][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX - i, self.posY))
            if not(matrix[self.posX - i][self.posY] == "00"):
                break
        for i in range(1,7):
            if(self.posY + i >= 8):
                break
            if not(matrix[self.posX][self.posY + i][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX, self.posY + i))
            if not(matrix[self.posX][self.posY + i] == "00"):
                break
        for i in range(1,7):
            if(self.posY - i < 0):
                break
            if not(matrix[self.posX][self.posY - i][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX, self.posY - i))
            if not(matrix[self.posX][self.posY - i] == "00"):
                break
        return available





