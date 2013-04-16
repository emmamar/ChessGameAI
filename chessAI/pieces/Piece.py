import copy
import sys
import cProfile

class Piece():

  def __init__(self, c, px, py):
    self.d = 1
    self.color = c
    self.posX = px
    self.posY = py
  
  def get_available_moves(self, board,px,py):
    posX = px
    posY = py
    test_set = self.get_available_moves_specific(board,posX,posY)
    available = list()
    
    for move in test_set:
      if self.not_check(board, move):
        available.append(move)
    return available

  def getPosX(self):
    return self.posX
  def getPosY(self):
    return self.posY
  
  def setPosX(self, px):
    return self.posX
  def setPosY(self, py):
    return self.posY
  

  def first_move(self):
    return False
  def set_first(self, arg):
    pass

  def not_check(self, board, move_to_try):
    can_move = board.try_move_piece(
      move_to_try
    )
    no_check = can_move and not board.is_check(self.color)
    board.undo()
    return no_check

  def get_color(self):
    return self.color