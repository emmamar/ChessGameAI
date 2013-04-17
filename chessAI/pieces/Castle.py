import Piece
from Move import Move

class Castle(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.table = None
    self.material = 750
    
  def get_available_moves_specific(self, board):
    available = list()

    for i in [1,2,3,4,5,6,7]:
      if self.posX + i > 7:
        break
      if(board.matrix[self.posX + i][self.posY] == None
      or not board.matrix[self.posX + i][self.posY].color == self.color):
        available.append(Move(self.posX, self.posY, self.posX + i, self.posY))
      if not board.matrix[self.posX + i][self.posY] == None:
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posX - i < 0:
        break
      if(board.matrix[self.posX - i][self.posY] == None
      or not board.matrix[self.posX - i][self.posY].color == self.color):
        available.append(Move(self.posX, self.posY, self.posX - i, self.posY))
      if not board.matrix[self.posX - i][self.posY] == None:
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posY + i > 7:
        break
      if(board.matrix[self.posX][self.posY + i] == None
      or not board.matrix[self.posX][self.posY + i].color == self.color):
        available.append(Move(self.posX, self.posY, self.posX, self.posY + i))
      if not board.matrix[self.posX][self.posY + i] == None:
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posY - i < 0:
        break
      if(board.matrix[self.posX][self.posY - i] == None
      or not board.matrix[self.posX][self.posY - i].color == self.color):
        available.append(Move(self.posX, self.posY, self.posX, self.posY - i))
      if not board.matrix[self.posX][self.posY - i] == None:
        break
    return available        
  
  def is_illegal(self, startX, startY, endX, endY, board):
    if( (not(startX - endX) == 0)
    and (startY - endY == 0)):
      length_of_move = startX - endX
      if (length_of_move < 0):
        range_var = -length_of_move
      else:
        range_var = length_of_move
      for i in range(1, range_var):
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
    elif(startX - endX == 0
    and (not (startY - endY) ==  0)):
      length_of_move = startY - endY
      if (length_of_move < 0):
        range_var = -length_of_move
      else:
        range_var = length_of_move
      for i in range(1, range_var):
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

