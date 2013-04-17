import Piece
from Move import Move

class Castle(Piece.Piece):
  def __init__(self, c):
    self.color = c
    self.first_move = True

  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()

    for i in range(1,7):
      if posX + i > 7:
        break
      if(board.matrix[posX + i][posY] == None
      or not board.matrix[posX + i][posY].color == self.color):
        available.append(Move(posX, posY, posX + i, posY))
      if not board.matrix[posX + i][posY] == None:
        break
    for i in range(1,7):
      if posX - i < 0:
        break
      if(board.matrix[posX - i][posY] == None
      or not board.matrix[posX - i][posY].color == self.color):
        available.append(Move(posX, posY, posX - i, posY))
      if not board.matrix[posX - i][posY] == None:
        break
    for i in range(1,7):
      if posY + i > 7:
        break
      if(board.matrix[posX][posY + i] == None
      or not board.matrix[posX][posY + i].color == self.color):
        available.append(Move(posX, posY, posX, posY + i))
      if not board.matrix[posX][posY + i] == None:
        break
    for i in range(1,7):
      if posY - i < 0:
        break
      if(board.matrix[posX][posY - i] == None
      or not board.matrix[posX][posY - i].color == self.color):
        available.append(Move(posX, posY, posX, posY - i))
      if not board.matrix[posX][posY - i] == None:
        break
    return available        
  
  def get_first_move(self):
    return self.first_move
  
  def set_first(self, arg):
    self.first_move = arg
  

  def is_illegal(self, startX, startY, endX, endY, board):
    if(abs(startX - endX) > 0
    and abs(startY - endY) == 0):
      length_of_move = startX - endX
      for i in range(1, abs(length_of_move)):
        if(length_of_move < 0):
          if(not board.matrix[startX + i][startY]
          == None):
            return True
        else:
          if(not board.matrix[startX - i][startY]
          == None):
            return True
      if(not board.matrix[startX - length_of_move]
      [startY] == None):
        if(board.matrix[startX - length_of_move]
        [startY].color == self.color):
          return True
        else:
          return False
      else:
        return False
    elif(abs(startX - endX) == 0
    and abs(startY - endY) > 0):
      length_of_move = startY - endY
      for i in range(1, abs(length_of_move)):
        if(length_of_move < 0):
          if(not board.matrix[startX][startY + i]
          == None):
            return True
        else:
          if(not board.matrix[startX][startY - i]
          == None):
            return True
      if(not board.matrix[startX]
      [startY - length_of_move] == None):
        if(board.matrix[startX]
        [startY - length_of_move].color == self.color):
          return True
        else:
          return False
      else:
        return False
    else:
      return True


  def toString(self):
    if self.color == "W":
      return "CW"
    else:
      return "CB"

