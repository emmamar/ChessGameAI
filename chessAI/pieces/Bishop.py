import Piece
from Move import Move

class Bishop(Piece.Piece):

  def __init__(self, c):
    self.color = c
        
  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()

    for i in range(1, 8 - posX):
      if posY + i <= 7:
        if(board.matrix[posX + i][posY + i] == None or not
          board.matrix[posX + i][posY + i].color == self.color):
          available.append(Move(posX,posY,posX + i, posY + i))
        if not board.matrix[posX + i][posY + i] == None:
          break
    for i in range(1, 8 - posX):
      if posY - i >= 0:
        if(board.matrix[posX + i][posY -i] == None or not
          board.matrix[posX + i][posY - i].color == self.color):
          available.append(Move(posX, posY, posX + i, posY - i))
        if not board.matrix[posX + i][posY - i] == None:
          break
    for i in range(1, posX):
      if posY + i <= 7:
        if(board.matrix[posX - i][posY + i] == None or not
          board.matrix[posX - i][posY + i].color == self.color):
          available.append(Move(posX, posY, posX - i, posY + i))
        if not board.matrix[posX - i][posY + i] == None:
          break
    for i in range(1, posX):
      if posY - i >= 0:
        if(board.matrix[posX - i][posY - i] == None or not
          board.matrix[posX - i][posY - i].color == self.color):
          available.append(Move(posX, posY, posX - i, posY - i))
        if not board.matrix[posX - i][posY - i] == None:
          break
    return available






  '''move already checks its within the board'''
  def is_illegal(self, startX, startY, endX, endY, board):
    if abs(startX - endX) == abs(startY - 
      endY):
      length_X = startX - endX
      length_Y = startY - endY
      for i in range(1, abs(length_X)):
        if length_X < 0:
          if length_Y < 0:
            if not (board.matrix[startX + i][startY + i]
            == None):
              return True
          else:
            if not (board.matrix[startX + i][startY - i]
            == None):
              return True
        elif length_X > 0:
          if length_Y < 0:
            if not (board.matrix[startX - i][startY + i]
            == None):
              return True
          else:
            if not (board.matrix[startX - i][startY - i]
            == None):
              return True
      if(not board.matrix[endX]
      [endY] == None):
        if(board.matrix[endX]
        [endY].color == self.color):
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


