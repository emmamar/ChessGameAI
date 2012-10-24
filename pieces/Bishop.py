import Piece

class Bishop(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.positionX = pX
        self.positionY = pY
        
    def get_available_moves(self, matrix):
        available = list()
        for i in range(1,7):
            if not(matrix[self.posX + 1][self.posY + 1][1:2] = self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY +1))       
            if not(matrix[self.posX + 1][self.posY - 1][1:2] = self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX + 1, self.posY -1))
            if not(matrix[self.posX - 1][self.posY + 1][1:2] = self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX -1, self.posY + 1))
            if not(matrix[self.posX - 1][self.posY - 1][1:2] = self.color):
                available.append(self.get_matrix_given_move(matrix, self.posX - 1, self.posY - 1))

        return available




