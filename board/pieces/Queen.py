import Piece
from Castle import Castle
from Bishop import Bishop
<<<<<<< HEAD


class Queen(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.bishop = Bishop(self.color, px, py)
    self.castle = Castle(self.color, px, py)
    self.table = None
    self.material = 800
    if (self.color == "W"):
      self.string_rep = "QW"
    else:
      self.string_rep = "QB"
    self.available_moves = None
    self.attacking = None
    self.refresh_on_change_squares = None
    self.table = [0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]
    
  def refresh_state(self, board):
    self.bishop.posX = self.posX
    self.castle.posX = self.posX
    self.bishop.posY = self.posY
    self.castle.posY = self.posY
    self.bishop.refresh_state(board)
    self.castle.refresh_state(board)
    self.available_moves = self.bishop.available_moves + self.castle.available_moves
    self.attacking = self.bishop.attacking + self.castle.attacking
    self.refresh_on_change_squares = self.bishop.refresh_on_change_squares + self.castle.refresh_on_change_squares
=======
from Move import Move

class Queen(Piece.Piece):
  def __init__(self, c):
    self.color = c
 
  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()
    bishop_instance = Bishop(self.color)
    castle_instance = Castle(self.color)
    available = (bishop_instance.get_available_moves(
                   board, px, py
                 ) +
                 castle_instance.get_available_moves(
                   board, px, py)
                 )

    return available

  def is_illegal(self, move, board):
    bishop_instance = Bishop(self.color)
    castle_instance = Castle(self.color)
    return (bishop_instance.is_illegal(move, board)
    and castle_instance.is_illegal(move, board))
      

  def toString(self):
    if self.color == "W":
      return "QW"
    else:
      return "QB"
>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4

