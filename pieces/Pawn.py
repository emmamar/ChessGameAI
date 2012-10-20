import Piece
import copy

class Pawn(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.posX = pX
        self.posY = pY
        self.first_move = 1

    '''returns a list of matricies of posible next boards if you 
    move this piece'''
    def get_available_moves(self, matrix):
        available = list()
        if(self.color == "B"):
            if (matrix[self.posX -1][self.posY] == "00"):
                available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY))
                if (self.first_move and matrix[self.posX - 2][self.posY] == "00"):
                    available.append(self.get_matrix_given_move(matrix, self.posX - 2, self.posY))
            if (self.posY < 7 and matrix[self.posX - 1][self.posY + 1][1:2] == "W"):
                available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY + 1))
            if (self.posY > 0 and matrix[self.posX - 1][self.posY - 1][1:2] == "W"):
                available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY - 1))
        else:
            if (matrix[self.posX + 1][self.posY] == "00"):
                available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY))
                if (self.first_move  and matrix[self.posX + 2][self.posY] == "00"):
                    available.append(self.get_matrix_given_move(matrix, self.posX + 2, self.posY))
            if (self.posY < 7 and matrix[self.posX + 1][self.posY + 1][1:2] == "B"):
                available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY + 1))
            if (self.posY > 0 and matrix[self.posX + 1][self.posY - 1][1:2] == "B"):
                available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY - 1))
        return available          

    


