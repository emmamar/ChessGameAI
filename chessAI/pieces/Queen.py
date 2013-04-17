import Piece
from Castle import Castle
from Bishop import Bishop


class Queen(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.bishop = Bishop(self.color, px, py)
    self.castle = Castle(self.color, px, py)
    self.table = None
    self.material = 1000
 
  def get_available_moves_specific(self, board):
    self.bishop.posX = self.posX
    self.castle.posX = self.posX
    self.bishop.posY = self.posY
    self.castle.posY = self.posY
    available = (self.bishop.get_available_moves_specific(
                   board) +
                 self.castle.get_available_moves_specific(
                   board))
    return available
      
  def is_illegal(self, startX, startY, endX, endY, board):
    return (self.bishop.is_illegal(startX, startY, endX, endY, board)
    and self.castle.is_illegal(startX, startY, endX, endY, board))

  def toString(self):
    if self.color == "W":
      return "QW"
    else:
      return "QB"

