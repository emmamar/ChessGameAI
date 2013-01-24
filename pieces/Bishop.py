import Piece

class Bishop(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.posX = pX
        self.posY = pY
        
    def get_available_moves(self, matrix):
        available = list()
        
        for i in range(1, 7 - self.posX):
            if(self.posY + i <= 7):
                if not(matrix[self.posX + i][self.posY + i][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX + i, self.posY + i))
                if not(matrix[self.posX + i][self.posY + i] == "00"):
                    break
        for i in range(1, 7 - self.posX):
            if(self.posY - i >= 0):
                if not(matrix[self.posX + i][self.posY - i][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX + i, self.posY - i))
                if not(matrix[self.posX + i][self.posY - i] == "00"):
                    break
        for i in range(1, self.posX):
            if(self.posY + i <= 7):
                if not(matrix[self.posX - i][self.posY + i][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX - i, self.posY + i))
                if not(matrix[self.posX - i][self.posY + i] == "00"):
                    break
        for i in range(1, self.posX):
            if(self.posY - i >= 0):   
                if not(matrix[self.posX - i][self.posY - i][1:2] == self.color):
                    available.append(self.get_matrix_given_move(matrix, self.posX - i, self.posY - i))
                if not(matrix[self.posX - i][self.posY - i] == "00"):
                    break

        return available




