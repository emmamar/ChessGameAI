from Move import Move
import copy
import numpy

'''this class creates a player object of a given color and of 
human or computer'''

class Player:
  '''constructor, takes color and wether human or computer'''
  def __init__ (self, c, dep = 0):
    '''create player'''
    self.color = c
    self.depth = dep

  '''determines the best next move for the computer player
  given the current board configuration'''
  def determineNextMove(self, board, best_sf):
    choises = self.get_all_available_moves(board)
    best_choise = None
    best_so_far = best_sf
    

    if len(choises) > 0:
      max_heuristic = None
      for choise in choises:

        if not(self.depth == 0):
          '''create an opponent to search, and decrement depth'''
          if self.color == "B":
            opponent = Player("W", (self.depth - 1))
          elif self.color == "W":
            opponent = Player("B", (self.depth - 1))
          
          '''opponent searches in a copy of the board with the
          choise played. gets their best move given the choise'''
          copy_of_board = copy.deepcopy(board)
          copy_of_board.try_move_piece(choise)
          print copy_of_board.toString() + self.color 
          min_max_best, min_max_heur = opponent.determineNextMove(
            copy_of_board, best_so_far
          )

          '''if((best_so_far == None)
          or (min_max_heur < best_so_far)):
            best_so_far = min_max_heur'''

          '''calculate the heuristic of the opponents best play
          given the choise'''
          '''copy_of_board2 = copy.deepcopy(board)
          copy_of_board2.try_move_piece(choise)
          best_heuristic = self.calculate_heuristic(
            copy_of_board2, min_max_best
          )'''
          best_heuristic = -min_max_heur
        else:
          best_heuristic = self.calculate_heuristic(
            copy.deepcopy(board), choise
          )

        '''calculate the optimal choise by max of their heuristics'''
        if(max_heuristic == None
        or best_heuristic > max_heuristic):
          max_heuristic = best_heuristic
          best_choise = choise
          '''alpha-beta pruning, pointless to continue'''
          if((not best_so_far == None)
          and (max_heuristic >= best_so_far)):
            return best_choise, max_heuristic
          elif ((best_so_far == None) or
          ((-best_heuristic) < best_so_far)):
            best_so_far = -best_heuristic
      return best_choise, max_heuristic

  '''helper function to determineNextMove that gets all the
  available next moves'''
  def get_all_available_moves(self, board):
    available_moves = list()
    for i in range(0, 8):
      for j in range(0, 8):
        if (not board.matrix[i][j] == None
        and board.matrix[i][j].color == self.color):
          per_piece = board.matrix[i][j].get_available_moves(
            board, i, j
          )
          for move in per_piece:
            available_moves.append(move)
    return available_moves

  '''helper function to determineNextMove that gets the
  heuristic value of a particualer move, given a copy
  of the board and a move'''
  def calculate_heuristic(self, board, move):
    board.try_move_piece(move)
    total_heuristic = 0
    for i in range(0,8):
      for j in range(0,8):
        total_heuristic += self.calc_material(board.matrix[i][j])
        total_heuristic += self.calc_piece_table_score(
          board.matrix[i][j], i, j
        )
    return total_heuristic

  def calc_material(self, piece):
    '''calculate the material of the board'''
    piece_value = {"King":5000, "Queen":1000, "Knight":500, "Bishop":500, 
    "Pawn":100, "Castle":750}
    if piece == None:
      return 0
    elif piece.color == self.color:
      return piece_value[piece.__class__.__name__]
    elif not piece.color == self.color:
      return -piece_value[piece.__class__.__name__]
    else:
      return 0

  def calc_mobility(self):
    pass

  def calc_doubled_blocked_isolated_pawns(self):
    pass

  def calc_piece_table_score(self, piece, posX, posY):
    piece_value = 0;
    if piece == None:
      return 0
    else:
      if piece.__class__.__name__ == "Pawn":
        if piece.color == "B":
          pawn_table = numpy.matrix('0   0   0   0   0   0  0  0;'
                                    '50 50  50  50  50  50 50 50;'
                                    '10 10  20  30  30  20 10 10;'
                                    '5   5  10  27  27  10  5  5;'
                                    '0   0   0  25  25   0  0  0;'
                                    '5  -5 -10   0   0 -10 -5  5;'
                                    '5  10  10 -25 -25  10 10  5;'
                                    '0   0   0   0   0   0  0  0')
        else:
          pawn_table = numpy.matrix('0   0   0   0   0   0   0   0;'
                                    '5  10  10 -25 -25  10 10  5;'
                                    '5  -5 -10   0   0 -10 -5  5;'
                                    '0   0   0  25  25   0  0  0;'
                                    '5   5  10  27  27  10  5  5;'
                                    '10 10  20  30  30  20 10 10;'
                                    '50 50  50  50  50  50 50 50;'
                                    '0   0   0   0   0   0  0  0')
                                    
        piece_value = pawn_table[posX, posY]
      elif piece.__class__.__name__ == "Knight":
        if piece.color == "B":
          knight_table = numpy.matrix('-50 -40 -30 -30 -30 -30 -40 -50;'
                                      '-40 -20  0  0  0  0 -20 -40;'
                                      '-30  0 10 15 15 10  0 -30;'
                                      '-30  5 15 20 20 15  5 -30;'
                                      '-30  0 15 20 20 15  0 -30;'
                                      '-30  5 10 15 15 10 5 -30;'
                                      '-40 -20  0 5  5  0 -20 -40;'
                                      '-50 -40 -20 -30 -30 -20 -40 -50')
        else:
          knight_table = numpy.matrix('-50 -40 -20 -30 -30 -20 -40 -50;'
                                      '-40 -20  0 5  5  0 -20 -40;'
                                      '-30  5 10 15 15 10 5 -30;'
                                      '-30  0 15 20 20 15  0 -30;'
                                      '-30  5 15 20 20 15  5 -30;'
                                      '-30  0 10 15 15 10  0 -30;'
                                      '-40 -20  0  0  0  0 -20 -40;'
                                      '-50 -40 -30 -30 -30 -30 -40 -50')

        piece_value = knight_table[posX, posY]
      elif piece.__class__.__name__ == "Bishop":
        if piece.color == "B":
          bishop_table = numpy.matrix('-20 -10 -10 -10 -10 -10 -10 -20;'
                                      '-10  0  0  0  0  0  0 -10;'
                                      '-10  0  5 10 10  5  0 -10;'
                                      '-10  5  5 10 10  5  5 -10;'
                                      '-10  0 10 10 10 10  0 -10;'
                                      '-10 10 10 10 10 10 10 -10;'
                                      '-10  5  0  0  0  0  5 -10;'
                                      '-20 -10 -40 -10 -10 -40 -10 -20')
        else:
          bishop_table = numpy.matrix('-20 -10 -40 -10 -10 -40 -10 -20;'
                                      '-10  5  0  0  0  0  5 -10;'
                                      '-10 10 10 10 10 10 10 -10;'
                                      '-10  0 10 10 10 10  0 -10;'
                                      '-10  5  5 10 10  5  5 -10;'
                                      '-10  0  5 10 10  5  0 -10;'
                                      '-10  0  0  0  0  0  0 -10;'
                                      '-20 -10 -10 -10 -10 -10 -10 -20')

        piece_value =  bishop_table[posX, posY]
      elif piece.__class__.__name__ == "King":
        if piece.color == "B":
          king_mid = numpy.matrix('-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-20 -30 -30 -40 -40 -30 -30 -20;'
                                  '-10 -20 -20 -20 -20 -20 -20 -10;'
                                  '20  20   0   0   0   0  20  20;'
                                  '20  30  10  0   0  10  30 20')
        else:
          king_mid = numpy.matrix('20  30  10  0   0  10  30 20;'
                                  '20  20   0   0   0   0  20  20;'
                                  '-10 -20 -20 -20 -20 -20 -20 -10;'
                                  '-20 -30 -30 -40 -40 -30 -30 -20;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30;'
                                  '-30 -40 -40 -50 -50 -40 -40 -30')
         
        '''king_table_end_game = 
        numpy.matrix([[-50,-40,-30,-20,-20,-30,-40,-50]
                                        [-30,-20,-10,  0,  0,-10,-20,-30]
                                        [-30,-10, 20, 30, 30, 20,-10,-30]
                                        [-30,-10, 30, 40, 40, 30,-10,-30]
                                        [-30,-10, 30, 40, 40, 30,-10,-30]
                                        [-30,-10, 20, 30, 30, 20,-10,-30]
                                        [-30,-30,  0,  0,  0,  0,-30,-30]
                                        [-50,-30,-30,-30,-30,-30,-30,-50]])
        '''
        piece_value = king_mid[posX, posY]


      else:
        return 0
      if (piece.color == self.color):
        return piece_value
      else:
        return -piece_value







