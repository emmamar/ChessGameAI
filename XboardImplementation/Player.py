from Move import Move


class Player:
    def __init__ (self, c):
        '''create player'''
        self.color = c

    def determineNextMove(self, board):
        choises = self.get_all_available_moves(board)
        best_choise = Move(3,3,3,3)
        if len(choises) > 0:
            max_heuristic = None
            for choise in choises: 
                heuristic = self.calculate_heuristic(board, choise)
                if max_heuristic == None or heuristic > max_heuristic:
                    max_heuristic = heuristic
                    best_choise = choise
            print best_choise.toString()
        return best_choise

    def get_all_available_moves(self, board):
        available_moves = list()
        for i in range(0, 8):
            for j in range(0, 8):
                if not board.matrix[i][j] == None and board.matrix[i][j].color == self.color:
                    per_piece = board.matrix[i][j].get_available_moves(board.matrix, i, j)
                    for moves in per_piece:
                        available_moves.append(moves)
        return available_moves


    def calculate_heuristic(self, board, move):
        board.move_piece(move)
        piece_value = {"King":5000, "Queen":100, "Knight":50, "Bishop":50, "Pawn":10, "Castle":75}
        heuristic = 0
        for i in range(0,8):
            for j in range(0,8):
                if board.matrix[i][j] == None:
                    heuristic = heuristic
                elif board.matrix[i][j].color == self.color:
                    heuristic = heuristic + piece_value[board.matrix[i][j].__class__.__name__]
                else:
                    heuristic = heuristic - piece_value[board.matrix[i][j].__class__.__name__]
        return heuristic






        


