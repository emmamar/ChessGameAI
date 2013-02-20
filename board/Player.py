from Move import Move
import copy

'''this class creates a player object of a given color and of 
human or computer'''

class Player:
  '''constructor, takes color and wether human or computer'''
  def __init__ (self, c, CH):
    '''create player'''
    self.color = c
    self.computer_or_human = CH
    
  '''determines the best next move for the computer player
  given the current board configuration'''
  def determineNextMove(self, board):
    choises = self.get_all_available_moves(board)
    best_choise = None
    if len(choises) > 0:
      max_heuristic = None
      for choise in choises:
        heuristic = self.calculate_heuristic(
          copy.deepcopy(board), choise
        )
        if(max_heuristic == None
        or heuristic > max_heuristic):
          max_heuristic = heuristic
          best_choise = choise
    return best_choise

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
  heuristic value of a particualer move'''
  def calculate_heuristic(self, board, move):
    board.try_move_piece(move)
    piece_value = {"King":5000, "Queen":100, "Knight":50, 
    "Bishop":50, "Pawn":10, "Castle":75}
    heuristic = 0
    for i in range(0,8):
      for j in range(0,8):
        if board.matrix[i][j] == None:
          heuristic = heuristic
        elif board.matrix[i][j].color == self.color:
           heuristic = (heuristic +
           piece_value[board.matrix[i][j].__class__.__name__])
        else:
          heuristic = (heuristic -
          piece_value[board.matrix[i][j].__class__.__name__])
    return heuristic



