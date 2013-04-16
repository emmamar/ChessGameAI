import Piece
from Castle import Castle
from Bishop import Bishop


class Queen(Piece.Piece):
  def __init__(self, c):
    self.color = c
    self.bishop = Bishop(self.color)
    self.castle = Castle(self.color)
 
  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = (self.bishop.get_available_moves_specific(
                   board, posX, posY
                 ) +
                 self.castle.get_available_moves_specific(
                   board, posX, posY)
                 )

    return available
      
  def is_illegal(self, startX, startY, endX, endY, board):
    return (self.bishop.is_illegal(startX, startY, endX, endY, board)
    and self.castle.is_illegal(startX, startY, endX, endY, board))

  def toString(self):
    if self.color == "W":
      return "QW"
    else:
      return "QB"
