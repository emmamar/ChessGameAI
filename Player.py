from Move import Move


class Player:
    def __init__ (self, c):
        '''create player'''
        self.color = c

    def determineNextMove(self, board_object):
        choises = self.get_all_available_moves(board_object.matrix)
        if len(choises) > 0:
            move_chosen = choises[0]
            print move_chosen.toString()
        else: 
            move_chosen = Move(3,3,3,3)
        return move_chosen 

    def get_all_available_moves(self, matrix):
        available_moves = list()
        for i in range(0, 7):
            for j in range(0, 7):
                if not matrix[i][j] == None and matrix[i][j].color == self.color:
                    per_piece = matrix[i][j].get_available_moves(matrix, i, j)
                    for moves in per_piece:
                        available_moves.append(moves)
        return available_moves





