import Piece

class Knight(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.posX = pX
        self.posY = pY


    def get_available_moves(self, matrix):
        available = list()
        if (self.posX - 1 >= 0):
            if(self.posY - 2 >= 0):
                if not (matrix[self.posX - 1][self.posY - 2][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY - 2))        
            if(self.posY + 2 <= 7):
                if not (matrix[self.posX - 1][self.posY + 2][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY + 2))

        if(self.posX - 2 >= 0):
            if(self.posY - 1 >= 0):
                if not (matrix[self.posX - 2][self.posY + 1][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX - 2, self.posY + 1))

            if(self.posY + 1 <= 7):
                if not (matrix[self.posX - 2][self.posY + 1][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX - 2, self.posY + 1))

        if(self.posX + 1 <= 7):
            if(self.posY - 2 >= 0):
                if not (matrix[self.posX + 1][self.posY - 2][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY - 2))

            if(self.posY + 2 <= 7):
                if not (matrix[self.posX + 1][self.posY + 2][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY + 2))

        if(self.posX + 2 <= 7):
            if(self.posY - 1 >= 0):
                if not (matrix[self.posX + 2][self.posY - 1][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX + 2, self.posY - 1))

            if(self.posY + 1 <= 7):
                if not (matrix[self.posX + 2][self.posY + 1][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX + 2, self.posY + 1))

        return available


