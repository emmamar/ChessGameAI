import Piece
from Move import Move

class King(Piece.Piece):
  def __init__(self, c):
    self.color = c

  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()

    if posX < 7:
      if(board.matrix[posX + 1][posY] == None
      or not board.matrix[posX + 1][posY].color == self.color):
        available.append(Move(posX, posY, posX + 1, posY))
      if posY > 0:
        if(board.matrix[posX + 1][posY - 1] == None or not
          board.matrix[posX + 1][posY - 1].color == self.color):
          available.append(Move(posX, posY, posX + 1, posY - 1))
      if posY < 7:
        if(board.matrix[posX + 1][posY + 1] == None or not
          board.matrix[posX + 1][posY + 1].color == self.color):
          available.append(Move(posX, posY, posX + 1, posY + 1))
    if posX > 0:
      if(board.matrix[posX - 1][posY] == None
      or not board.matrix[posX - 1][posY].color == self.color):
        available.append(Move(posX, posY, posX - 1, posY))
      if posY > 0:
        if(board.matrix[posX - 1][posY -1] == None or not
        board.matrix[posX - 1][posY -1].color == self.color):
          available.append(Move(posX, posY, posX - 1, posY - 1))
      if posY < 7:
        if(board.matrix[posX - 1][posY + 1] == None or not
          board.matrix[posX - 1][posY + 1].color == self.color):
          available.append(Move(posX, posY, posX - 1, posY + 1))
    if posY < 7:
      if(board.matrix[posX][posY + 1] == None or not
        board.matrix[posX][posY + 1].color == self.color):
        available.append(Move(posX, posY, posX, posY + 1))
    if posY > 0:
      if(board.matrix[posX][posY - 1] == None or not
        board.matrix[posX][posY - 1].color == self.color):
        available.append(Move(posX, posY, posX, posY - 1))
    return available

  def is_illegal(self, move, board):
    if(((abs(move.startX - move.endX) <= 1
    and abs(move.startY - move.endY) == 1)
    or (abs(move.startX - move.endX) == 1
    and abs(move.startY - move.endY <= 1)))
    and (board.matrix[move.endX][move.endY] == None
    or not board.matrix[move.endX][move.endY].color
    == self.color)):
      return False
    else:
      return True

  def toString(self):
    if self.color == "W":
      return "KW"
    else:
      return "KB"
