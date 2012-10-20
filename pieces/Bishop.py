import Piece

class Bishop(Piece.Piece):

    def __init__(self, c, pX, pY):
        self.color = c
        self.positionX = pX
        self.positionY = pY
        
    def get_available_moves(self, matrix):
        available = list()
        if(self.color == "w"):
             available.append(matrix)
        elif(self.color == "B"):
            available.append(matrix)

        return available


    def get_matrix_given_move(self, matrix, pX2, pY2):
        matrix_moved = copy.deepcopy(matrix)
        temp = matrix_moved[self.posX][self.posY]
        matrix_moved[self.posX][self.posY] = matrix_moved[pX2][pY2]
        matrix_moved[pX2][pY2] = temp
        return matrix_moved





