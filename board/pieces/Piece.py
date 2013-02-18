import copy
import sys

class Piece():

  def __init__(self, c):
    self.d = 1
    self.color = c

  def check_if_not_check(self, board, move_to_try):
    check_board = copy.deepcopy(board)
    can_move = check_board.try_move_piece(
      move_to_try
    )
    if(can_move and not check_board.is_check(self.color)):
      return True
    else:
      return False
