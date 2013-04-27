import copy

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
    choises_per_piece = [None]*16
    if(self.color == "B"):
      for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        choises_per_piece[i] = board.available_moves_black[i]
    else:
      for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
        choises_per_piece[i] = board.available_moves_white[i]
    max_heur_of_all_choises = None
    best_choise_of_all = None
    alpha_beta_list = ab_list
    opponent_heur = None
    found_choise = False
    
    for choises in choises_per_piece:
      if(not choises == None):
        if len(choises) > 0:
          found_choise = True
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
              board.try_move_piece(choise)
              '''print board.to_string()'''
              my_heur_for_choise = self.calculate_heuristic(
                board
              )
              board.undo()


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
    if(found_choise):
      return best_choise_of_all, max_heur_of_all_choises
    else:
      return None, None 


  '''helper function to determineNextMove that gets the
  heuristic value of a particuler move, given a copy
  of the board and a move'''
  def calculate_heuristic(self, board):
    total_heuristic = 0
    end_white = (board.white_piece_count < 9)
    end_black = (board.black_piece_count < 9)
    i = 0
    for piece in board.black_pieces:
      if(not piece == None):
        total_heuristic += self.calc_material(piece)
        total_heuristic += self.calc_piece_table_score(
          piece, piece.posX, piece.posY, end_black
        )
        for attack in board.attacking_black[i]:
          if(self.color == "B"):
            total_heuristic += (0.5) * attack.material
          else:
            total_heuristic += (-0.5) * attack.material
      i += 1
    i = 0
    for piece in board.white_pieces:
      if(not piece == None):
        total_heuristic += self.calc_material(piece)
        total_heuristic += self.calc_piece_table_score(
          piece, piece.posX, piece.posY, end_white
        )
        for attack in board.attacking_white[i]:
          if(self.color == "W"):
            total_heuristic += (0.5) * attack.material
          else:
            total_heuristic += (-0.5) * attack.material
      i += 1
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

  def calc_piece_table_score(self, piece, posX, posY, end):
    piece_value = 0         
    if(not piece.table == None):
      if(end and (piece.__class__.__name__ == "King")):
        piece_value = piece.table_end[(posX*8) +  posY]
      else:
        piece_value = piece.table[(posX*8) +  posY]
      if (piece.color == self.color):
        return piece_value
      else:
        return -piece_value
    else:
      return piece_value






