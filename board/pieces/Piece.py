<<<<<<< HEAD

class Piece():

  def __init__(self, c, px, py):
    pass
  
  def get_available_moves(self, board):
    test_set = self.available_moves
=======
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
>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4
    available = list()

    for move in test_set:
      if self.not_check(board, move):
<<<<<<< HEAD
        available += move
    return available

  def not_check(self, board, move_to_try):
    can_move = board.try_move_piece(
      move_to_try
    )
    no_check = can_move and not board.is_check(self.color)
    board.undo()
    return no_check
  
  
=======
        available.append(move)
    return available


  def not_check(self, board, move_to_try):
    check_board = copy.deepcopy(board)
    can_move = check_board.try_move_piece(
      move_to_try
    )
    return (can_move and not check_board.is_check(self.color))
>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4
