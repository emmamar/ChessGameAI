import Piece
from Move import Move

class Bishop(Piece.Piece):

  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py   
    self.first_move = True
    self.material = 500
    if( self.color == "B"):
      self.table = [-20, -10, -10, -10, -10, -10, -10, -20,
                              -10,   0,   0,   0,   0,   0,   0, -10,
                              -10,   0,   5,  10,  10,   5,   0, -10,
                              -10,   5,   5,  10,  10,   5,   5, -10,
                              -10,   0,  10,  10,  10,  10,   0, -10,
                              -10,  10,  10,  10,  10,  10,  10, -10,
                              -10,   5,   0,   0,   0,   0,   5, -10,
                              -20, -10, -40, -10, -10, -40, -10, -20]
    else:
      self.table = [-20, -10, -40, -10, -10, -40, -10, -20,
                          -10,   5,   0,   0,   0,   0,   5, -10,
                          -10,  10,  10,  10,  10,  10,  10, -10,
                          -10,   0,  10,  10,  10,  10,   0, -10,
                          -10,   5,   5,  10,  10,   5,   5, -10,
                          -10,   0,   5,  10,  10,   5,   0, -10,
                          -10,   0,   0,   0,   0,   0,   0, -10,
                          -20, -10, -10, -10, -10, -10, -10, -20]
        
  def get_available_moves_specific(self, board):
    available = list()
    for i in range(1, 8 - self.posX):
      if self.posY + i <= 7:
        if(board.matrix[self.posX + i][self.posY + i] == None or not
          board.matrix[self.posX + i][self.posY + i].color == self.color):
          available.append(Move(self.posX,self.posY,self.posX + i, self.posY + i))
        if not board.matrix[self.posX + i][self.posY + i] == None:
          break
    for i in range(1, 8 - self.posX):
      if self.posY - i >= 0:
        if(board.matrix[self.posX + i][self.posY -i] == None or not
          board.matrix[self.posX + i][self.posY - i].color == self.color):
          available.append(Move(self.posX, self.posY, self.posX + i, self.posY - i))
        if not board.matrix[self.posX + i][self.posY - i] == None:
          break
    for i in range(1, self.posX):
      if self.posY + i <= 7:
        if(board.matrix[self.posX - i][self.posY + i] == None or not
          board.matrix[self.posX - i][self.posY + i].color == self.color):
          available.append(Move(self.posX, self.posY, self.posX - i, self.posY + i))
        if not board.matrix[self.posX - i][self.posY + i] == None:
          break
    for i in range(1, self.posX):
      if self.posY - i >= 0:
        if(board.matrix[self.posX - i][self.posY - i] == None or not
          board.matrix[self.posX - i][self.posY - i].color == self.color):
          available.append(Move(self.posX, self.posY, self.posX - i, self.posY - i))
        if not board.matrix[self.posX - i][self.posY - i] == None:
          break
    return available

  '''move already checks its within the board'''
  def is_illegal(self, startX, startY, endX, endY, board):
    if ((startX - endX == startY - endY) 
    or (startX - endX == -(startY - endY))):
      length_X = startX - endX
      length_Y = startY - endY
      if(length_X < 0):
        torange = -length_X
      else:
        torange = length_X
      for i in range(1, torange):
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


