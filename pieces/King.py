import Piece
import copy

class King(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.posX = pX
        self.posY = pY


    def get_available_moves(self, matrix):
        available = list()
        if (self.posX < 7):
            if not (matrix[self.posX + 1][self.posY][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY))
        if (self.posX > 0):
            if not (matrix[self.posX - 1][self.posY][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY))
        if (self.posY < 7):
            if not (matrix[self.posX][self.posY + 1][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX, self.posY + 1))
        if (self.posY > 0):
            if not (matrix[self.posX][self.posY - 1][1:2] == self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX, self.posY - 1))
        return available
        

