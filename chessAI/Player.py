
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
    if(self.color == "B"):
      for piece in board.get_black():
        per_piece = piece.get_available_moves(
          board)
        for move in per_piece:
          available_moves.append(move)
    elif(self.color == "W"):
      for piece in board.get_white():
        per_piece = piece.get_available_moves(
          board)
        for move in per_piece:
          available_moves.append(move)
    return available_moves

  '''helper function to determineNextMove that gets the
  heuristic value of a particuler move, given a copy
  of the board and a move'''
  def calculate_heuristic(self, board, move):
    board.try_move_piece(move)
    total_heuristic = 0
    for piece in board.get_black():
      total_heuristic += self.calc_material(piece)
      total_heuristic += self.calc_piece_table_score(
        piece, piece.posX, piece.posY
      )
    for piece in board.get_white():
      total_heuristic += self.calc_material(piece)
      total_heuristic += self.calc_piece_table_score(
        piece, piece.posX, piece.posY
      )
    board.undo()
    return total_heuristic

  def calc_material(self, piece):
    '''calculate the material of the board'''
    if piece.color == self.color:
      return piece.material
    else:
      return -piece.material


  def calc_mobility(self):
    pass

  def calc_doubled_blocked_isolated_pawns(self):
    pass

  def calc_piece_table_score(self, piece, posX, posY):
    piece_value = 0         
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
    if(not piece.table == None):
      piece_value = piece.table[(posX*8) +  posY]
      if (piece.color == self.color):
        return piece_value
      else:
        return -piece_value
    else:
      return piece_value







