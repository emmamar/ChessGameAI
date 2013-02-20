import copy
import sys

class Piece():

  def __init__(self, c):
    self.d = 1
    self.color = c
  
  def get_available_moves(self, board,px,py):
    posX = px
    posY = py
    test_set = self.get_available_moves_specific(board,px,py)
    available = list()

    for move in test_set:
      if self.not_check(board, move):
        available.append(move)
    return available


  def not_check(self, board, move_to_try):
    check_board = copy.deepcopy(board)
    can_move = check_board.try_move_piece(
      move_to_try
    )
    return (can_move and not check_board.is_check(self.color))
