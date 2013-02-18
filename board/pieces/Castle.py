import Piece
from Move import Move

class Castle(Piece.Piece):
  def __init__(self, c):
    self.color = c

  def get_available_moves(self, board, px, py):
    posX = px
    posY = py
    available = list()

    for i in range(1,7):
      if posX + i >= 8:
        break
      if(board.matrix[posX + i][posY] == None
      or not board.matrix[posX + i][posY].color == self.color):
        move_to_try = Move(posX, posY, posX + i, posY)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
      if not board.matrix[posX + i][posY] == None:
        break
    for i in range(1,7):
      if posX - i < 0:
        break
      if(board.matrix[posX - i][posY] == None
      or not board.matrix[posX - i][posY].color == self.color):
        move_to_try = Move(posX, posY, posX - i, posY)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
      if not board.matrix[posX - i][posY] == None:
        break
    for i in range(1,7):
      if posY + i >= 8:
        break
      if(board.matrix[posX][posY + i] == None
      or not board.matrix[posX][posY + i].color == self.color):
        move_to_try =Move(posX, posY, posX, posY + i)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
      if not board.matrix[posX][posY + i] == None:
        break
    for i in range(1,7):
      if posY - i < 0:
        break
      if(board.matrix[posX][posY - i] == None
      or not board.matrix[posX][posY - i].color == self.color):
        move_to_try = Move(posX, posY, posX, posY - i)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
      if not board.matrix[posX][posY - i] == None:
        break
    return available        
  
  def is_illegal(self, move, board):
    if abs(move.startX - move.endX) > 0:
      length_of_move = move.startX - move.endX
      for i in range(1, abs(length_of_move)):
        if(length_of_move < 0):
          if(not board.matrix[move.startX + i][move.startY]
          == None):
            return True
        else:
          if(not board.matrix[move.startX - i][move.startY]
          == None):
            return True
      if not board.matrix[move.endX][move.endY] == None:
        if(board.matrix[move.endX][move.endY].color ==
          self.color):
          return True
        else:
          return False
      else:
        return False
    else:
      length_of_move = move.startY - move.endY
      for i in range(1, abs(length_of_move)):
        if(length_of_move < 0):
          if(not board.matrix[move.startX][move.startY + i]
          == None):
            return True
        else:
          if(not board.matrix[move.startX][move.startY - i]
          == None):
            return True
      if not board.matrix[move.endX][move.endY] == None:
        if(board.matrix[move.endX][move.endY].color ==
          self.color):
          return True
        else:
          return False
      else:
        return False


  def toString(self):
    if self.color == "W":
      return "CW"
    else:
      return "CB"

