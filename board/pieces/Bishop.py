import Piece
from Move import Move

class Bishop(Piece.Piece):

  def __init__(self, c):
    self.color = c
        
  def get_available_moves(self, board, px, py):
    posX = px
    posY = py
    available = list()

    for i in range(1, 7 - posX):
      if posY + i <= 7:
        if(board.matrix[posX + i][posY + i] == None
        or not board.matrix[posX + i][posY + i].color == self.color):
          move_to_try = Move(posX,posY,posX + i, posY + i)
          if self.check_if_not_check(board, move_to_try):
            available.append(move_to_try)
        if not board.matrix[posX + i][posY + i] == None:
          break
    for i in range(1, 7 - posX):
      if posY - i >= 0:
        if(board.matrix[posX + i][posY -i] == None
        or not board.matrix[posX + i][posY - i].color == self.color):
          move_to_try = Move(posX, posY, posX + i, posY - i)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
        if not board.matrix[posX + i][posY - i] == None:
          break
    for i in range(1, posX):
      if posY + i <= 7:
        if(board.matrix[posX - i][posY + i] == None
        or not board.matrix[posX - i][posY + i].color == self.color):
          move_to_try =Move(posX, posY, posX - i, posY + i)
          if self.check_if_not_check(board, move_to_try):
            available.append(move_to_try)
        if not board.matrix[posX - i][posY + i] == None:
          break
    for i in range(1, posX):
      if posY - i >= 0:
        if(board.matrix[posX - i][posY - i] == None
        or not board.matrix[posX - i][posY - i].color == self.color):
          move_to_try =Move(posX, posY, posX - i, posY - i)
          if self.check_if_not_check:
            available.append(move_to_try)
        if not board.matrix[posX - i][posY - i] == None:
          break
    return available




  '''move already checks its within the board'''
  def is_illegal(self, move, board):
    if (move.startX - move.endX) == (move.startY - move.endY):
      sq_length_of_move = move.startX - move.endX
      for i in range(1, abs(sq_length_of_move)):
        if sq_length_of_move < 0:
          if not (board.matix[move.startX + i][move.startY + i]
          == None):
            return True
        else:
          if not (board.matrix[move.startX - i][move.startY - i]
          == None):
            return True
      if(not board.matrix[move.endX][move.endY] == None):
        if(board.matrix[move.endX][move.endY].color == self.color):
          return True
        else:
          return False
      else:
        return False
    else:
      return True

  def toString(self):
    if self.color == "W":
      return "BW"
    else:
      return "BB"


