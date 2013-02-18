import Piece
from Move import Move

class Knight(Piece.Piece):
  def __init__(self, c):
    self.color = c

  def get_available_moves(self, board, px, py):
    posX = px
    posY = py
    available = list()
    if posX - 1 >= 0:
      if posY - 2 >= 0:
        if(board.matrix[posX - 1][posY - 2] == None
        or not board.matrix[posX - 1][posY - 2].color == self.color):
          move_to_try = Move(posX, posY, posX - 1, posY - 2)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
      if posY + 2 <= 7:
        if(board.matrix[posX - 1][posY + 2] == None
        or not board.matrix[posX - 1][posY + 2].color == self.color):
          move_to_try = Move(posX, posY, posX - 1, posY + 2)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
    if posX - 2 >= 0:
      if posY - 1 >= 0:
        if(board.matrix[posX - 2][posY + 1] == None
        or not board.matrix[posX - 2][posY + 1].color == self.color):
          move_to_try = Move(posX, posY, posX - 2, posY + 1)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
      if posY + 1 <= 7:
        if(board.matrix[posX - 2][posY + 1] == None
        or not board.matrix[posX - 2][posY + 1].color == self.color):
          move_to_try = Move(posX, posY, posX - 2, posY + 1)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
    if posX + 1 <= 7:
      if posY - 2 >= 0:
        if(board.matrix[posX + 1][posY - 2] == None
        or not board.matrix[posX + 1][posY - 2].color == self.color):
          move_to_try = Move(posX, posY, posX + 1, posY - 2)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
      if posY + 2 <= 7:
        if(board.matrix[posX + 1][posY + 2] == None
        or not board.matrix[posX + 1][posY + 2].color == self.color):
          move_to_try = Move(posX, posY, posX + 1, posY + 2)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
    if posX + 2 <= 7:
      if posY - 1 >= 0:
        if(board.matrix[posX + 2][posY - 1] == None
        or not board.matrix[posX + 2][posY - 1].color == self.color):
          move_to_try = Move(posX, posY, posX + 2, posY - 1)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
      if posY + 1 <= 7:
        if(board.matrix[posX + 2][posY + 1] == None
        or not board,matrix[posX + 2][posY + 1].color == self.color):
          move_to_try = Move(posX, posY, posX + 2, posY + 1)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)

    return available

  def is_illegal(self, move, board):
    if(board.matrix[move.endX][move.endY] == None
    or not board.matrix[move.endX][move.endY].color
    == self.color):
      if(abs(move.startX - move.endX) == 2
      and abs(move.startY - move.endY) == 1):
        return False
      elif(abs(move.startY - move.endY) == 2
      and abs(move.startX - move.endX) == 1):
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






