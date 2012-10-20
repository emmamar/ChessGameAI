import copy

class Piece():

    def __init__(self):
        self.d = 1


    def get_matrix_given_move(self, matrix, pX2, pY2):
        matrix_moved = copy.deepcopy(matrix)
        matrix_moved[pX2][pY2] = matrix_moved[self.posX][self.posY]
        matrix_moved[self.posX][self.posY] = "00"
        return matrix_moved

