from Move import Move
import copy
import cProfile


'''cProfile.runctx( "self.calculate_heuristic(board, choise)", 
globals(), locals(), 
filename="/home/emma/Desktop/emmaPython.profile" )'''

'''this class creates a player object of a given color and of 
human or computer'''

class Player:
  '''constructor, takes color and depth'''
  def __init__ (self, c, dep = 0):
    '''create player'''
    self.color = c
    self.depth = dep

  '''determines the best next move for the computer player
  given the current board configuration'''
  def determineNextMove(self, board, ab_list):
    choises = self.get_all_available_moves(board)
    max_heur_of_all_choises = None
    best_choise_of_all = None
    alpha_beta_list = ab_list
    opponent_heur = None
    
    if len(choises) > 0:
      for choise in choises:
        if not(self.depth == 0):
          if self.color == "B":
            opponent = Player("W", (self.depth - 1))
          elif self.color == "W":
            opponent = Player("B", (self.depth - 1))

          board.try_move_piece(choise)
          opponent_choise, opponent_heur = opponent.determineNextMove(
            board, alpha_beta_list[1:]
          )
          board.undo()
          if (not opponent_heur == None):
            my_heur_for_choise = -opponent_heur
          elif (self.color == "B"):
            return choise, 99999999
          else:
            return choise, -99999999
        else:
          my_heur_for_choise = self.calculate_heuristic(
            board, choise
          )
        if ((not alpha_beta_list[0] == None)
        and alpha_beta_list[0] <= my_heur_for_choise):
          return choise, my_heur_for_choise
        if(max_heur_of_all_choises == None):
          max_heur_of_all_choises = my_heur_for_choise
          best_choise_of_all = choise
        elif (max_heur_of_all_choises < my_heur_for_choise):
          max_heur_of_all_choises = my_heur_for_choise
          best_choise_of_all = choise
        if(not opponent_heur == None):
          if(alpha_beta_list[1] == None
          or alpha_beta_list[1] > opponent_heur):
            alpha_beta_list[1] = opponent_heur
      return best_choise_of_all, max_heur_of_all_choises
    
    
    else:
      return None, None 


  '''helper function to determineNextMove that gets all the
  available next moves'''
  def get_all_available_moves(self, board):
    available_moves = list()
    for i in [0,1,2,3,4,5,6,7]:
      for j in [0,1,2,3,4,5,6,7]:
        if (not board.matrix[i][j] == None
        and board.matrix[i][j].color == self.color):
          per_piece = board.matrix[i][j].get_available_moves(
            board, i, j
          )
          for move in per_piece:
            available_moves.append(move)
    return available_moves

  '''helper function to determineNextMove that gets the
  heuristic value of a particuler move, given a copy
  of the board and a move'''
  def calculate_heuristic(self, board, move):
    board.try_move_piece(move)
    total_heuristic = 0
    for i in [0,1,2,3,4,5,6,7]:
      for j in [0,1,2,3,4,5,6,7]:
        if(not board.matrix[i][j] == None):
          total_heuristic += self.calc_material(board.matrix[i][j])
          total_heuristic += self.calc_piece_table_score(
            board.matrix[i][j], i, j
          )
    board.undo()
    return total_heuristic

  def calc_material(self, piece):
    '''calculate the material of the board'''
    piece_value = {"King":5000, "Queen":1000, "Knight":500, "Bishop":500, 
    "Pawn":100, "Castle":750}
    if piece.color == self.color:
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
          pawn_table = [0,   0,   0,   0,   0,   0,  0,  0,
                            50, 50,  50,  50,  50,  50, 50, 50,
                            10, 10,  20,  30,  30,  20, 10, 10,
                            5,   5,  10,  27,  27,  10,  5,  5,
                            0,   0,   0,  25,  25,   0,  0,  0,
                            5,  -5, -10,   0,   0, -10, -5,  5,
                            5,  10,  10, -25, -25,  10, 10,  5,
                            0,   0,   0,   0,   0,   0,  0,  0]
        else:
          pawn_table = [0,   0,   0,   0,   0,   0,   0,   0,
                            5,  10,  10, -25, -25,  10,  10,   5,
                            5,  -5, -10,   0,   0, -10,  -5,   5,
                            0,   0,   0,  25,  25,   0,   0,   0,
                            5,   5,  10,  27,  27,  10,   5,   5,
                           10,  10,  20,  30,  30,  20,  10,  10,
                           50,  50,  50,  50,  50,  50,  50,  50,
                            0,   0,   0,   0,   0,   0,   0,   0]
                                    
        piece_value = pawn_table[(posX*8) +  posY]
      elif piece.__class__.__name__ == "Knight":
        if piece.color == "B":
          knight_table = [-50, -40, -30, -30, -30, -30, -40, -50,
                              -40, -20,   0,   0,   0,   0, -20, -40,
                              -30,   0,  10,  15,  15,  10,   0, -30,
                              -30,   5,  15,  20,  20,  15,   5, -30,
                              -30,   0,  15,  20,  20,  15,   0, -30,
                              -30,   5,  10,  15,  15,  10,   5, -30,
                              -40, -20,   0,   5,   5,   0, -20, -40,
                              -50, -40, -20, -30, -30, -20, -40, -50]
        else:
          knight_table = [-50, -40, -20, -30, -30, -20, -40, -50,
                              -40, -20,   0,   5,   5,   0, -20, -40,
                              -30,   5,  10,  15,  15,  10,   5, -30,
                              -30,   0,  15,  20,  20,  15,   0, -30,
                              -30,   5,  15,  20,  20,  15,   5, -30,
                              -30,   0,  10,  15,  15,  10,   0, -30,
                              -40, -20,   0,   0,   0,   0, -20, -40,
                              -50, -40, -30, -30, -30, -30, -40, -50]

        piece_value = knight_table[(posX*8) +  posY]
      elif piece.__class__.__name__ == "Bishop":
        if piece.color == "B":
          bishop_table = [-20, -10, -10, -10, -10, -10, -10, -20,
                              -10,   0,   0,   0,   0,   0,   0, -10,
                              -10,   0,   5,  10,  10,   5,   0, -10,
                              -10,   5,   5,  10,  10,   5,   5, -10,
                              -10,   0,  10,  10,  10,  10,   0, -10,
                              -10,  10,  10,  10,  10,  10,  10, -10,
                              -10,   5,   0,   0,   0,   0,   5, -10,
                              -20, -10, -40, -10, -10, -40, -10, -20]
        else:
          bishop_table = [-20, -10, -40, -10, -10, -40, -10, -20,
                          -10,   5,   0,   0,   0,   0,   5, -10,
                          -10,  10,  10,  10,  10,  10,  10, -10,
                          -10,   0,  10,  10,  10,  10,   0, -10,
                          -10,   5,   5,  10,  10,   5,   5, -10,
                          -10,   0,   5,  10,  10,   5,   0, -10,
                          -10,   0,   0,   0,   0,   0,   0, -10,
                          -20, -10, -10, -10, -10, -10, -10, -20]

        piece_value =  bishop_table[(posX*8) +  posY]
      elif piece.__class__.__name__ == "King":
        if piece.color == "B":
          king_mid = [-30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -20, -30, -30, -40, -40, -30, -30, -20,
                          -10, -20, -20, -20, -20, -20, -20, -10,
                           20,  20,   0,   0,   0,   0,  20,  20,
                           20,  30,  10,   0,   0,  10,  30, 20]
        else:
          king_mid = [20,  30,  10,  0,   0,  10,  30, 20,
                          20,  20,   0,   0,   0,   0,  20,  20,
                          -10, -20, -20, -20, -20, -20, -20, -10,
                          -20, -30, -30, -40, -40, -30, -30, -20,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30]
         
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
        piece_value = king_mid[(posX*8) +  posY]


      else:
        return 0
      if (piece.color == self.color):
        return piece_value
      else:
        return -piece_value






