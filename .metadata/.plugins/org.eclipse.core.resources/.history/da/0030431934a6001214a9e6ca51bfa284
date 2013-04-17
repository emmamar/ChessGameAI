import Piece
from Move import Move

class Knight(Piece.Piece):
  def __init__(self, c):
    self.color = c

  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()
    if posX - 1 >= 0:
      if posY - 2 >= 0:
        if(board.matrix[posX - 1][posY - 2] == None or not
          board.matrix[posX - 1][posY - 2].color == self.color):
          available.append(Move(posX, posY, posX - 1, posY - 2))
      if posY + 2 < 8:
        if(board.matrix[posX - 1][posY + 2] == None or not
          board.matrix[posX - 1][posY + 2].color == self.color):
          available.append(Move(posX, posY, posX - 1, posY + 2))
    if posX - 2 >= 0:
      if posY - 1 >= 0:
        if(board.matrix[posX - 2][posY - 1] == None or not
          board.matrix[posX - 2][posY - 1].color == self.color):
          available.append(Move(posX, posY, posX - 2, posY - 1))
      if posY + 1 < 8:
        if(board.matrix[posX - 2][posY + 1] == None or not
          board.matrix[posX - 2][posY + 1].color == self.color):
          available.append(Move(posX, posY, posX - 2, posY + 1))
    if posX + 1 < 8:
      if posY - 2 >= 0:
        if(board.matrix[posX + 1][posY - 2] == None or not
          board.matrix[posX + 1][posY - 2].color == self.color):
          available.append(Move(posX, posY, posX + 1, posY - 2))
      if posY + 2 < 8:
        if(board.matrix[posX + 1][posY + 2] == None or not
          board.matrix[posX + 1][posY + 2].color == self.color):
          available.append(Move(posX, posY, posX + 1, posY + 2))
    if posX + 2 < 8:
      if posY - 1 >= 0:
        if(board.matrix[posX + 2][posY - 1] == None or not
          board.matrix[posX + 2][posY - 1].color == self.color):
          available.append(Move(posX, posY, posX + 2, posY - 1))
      if posY + 1 < 8:
        if(board.matrix[posX + 2][posY + 1] == None or not
          board.matrix[posX + 2][posY + 1].color == self.color):
          available.append(Move(posX, posY, posX + 2, posY + 1))

    return available

  def is_illegal(self, startX, startY, endX, endY, board):
    if(board.matrix[endX][endY] == None
    or not board.matrix[endX][endY].color
    == self.color):
      if(abs(startX - endX) == 2
      and abs(startY - endY) == 1):
        return False
      elif(abs(startY - endY) == 2
      and abs(startX - endX) == 1):
        return False
      else:
        return True
    else:
      return True

  def toString(self):
    if self.color == "W":
      return "RW"
    else:
      return "RB"






