import Piece
from Move import Move

class Knight(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.material = 500
    if (self.color == "W"):
      self.string_rep = "RW"
    else:
      self.string_rep = "RB"
    if(self.color == "B"):
      self.table = [-50, -40, -30, -30, -30, -30, -40, -50,
                              -40, -20,   0,   0,   0,   0, -20, -40,
                              -30,   0,  10,  15,  15,  10,   0, -30,
                              -30,   5,  15,  20,  20,  15,   5, -30,
                              -30,   0,  15,  20,  20,  15,   0, -30,
                              -30,   5,  10,  15,  15,  10,   5, -30,
                              -40, -20,   0,   5,   5,   0, -20, -40,
                              -50, -40, -20, -30, -30, -20, -40, -50]
    else:
      self.table = [-50, -40, -20, -30, -30, -20, -40, -50,
                              -40, -20,   0,   5,   5,   0, -20, -40,
                              -30,   5,  10,  15,  15,  10,   5, -30,
                              -30,   0,  15,  20,  20,  15,   0, -30,
                              -30,   5,  15,  20,  20,  15,   5, -30,
                              -30,   0,  10,  15,  15,  10,   0, -30,
                              -40, -20,   0,   0,   0,   0, -20, -40,
                              -50, -40, -30, -30, -30, -30, -40, -50]

  def get_available_moves_specific(self, board):
    available = list()
    if self.posX - 1 >= 0:
      if self.posY - 2 >= 0:
        if((board.matrix[self.posX - 1][self.posY - 2] == None)
        or (not board.matrix[self.posX - 1][self.posY - 2].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX - 1, self.posY - 2))
      if self.posY + 2 <= 7:
        if(board.matrix[self.posX - 1][self.posY + 2] == None
        or (not board.matrix[self.posX - 1][self.posY + 2].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX - 1, self.posY + 2))
    if self.posX - 2 >= 0:
      if self.posY - 1 >= 0:
        if(board.matrix[self.posX - 2][self.posY - 1] == None
        or (not board.matrix[self.posX - 2][self.posY - 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX - 2, self.posY - 1))
      if self.posY + 1 <= 7:
        if(board.matrix[self.posX - 2][self.posY + 1] == None
        or (not board.matrix[self.posX - 2][self.posY + 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX - 2, self.posY + 1))
    if self.posX + 1 <= 7:
      if self.posY - 2 >= 0:
        if(board.matrix[self.posX + 1][self.posY - 2] == None
        or (not board.matrix[self.posX + 1][self.posY - 2].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX + 1, self.posY - 2))
      if self.posY + 2 <= 7:
        if(board.matrix[self.posX + 1][self.posY + 2] == None
        or (not board.matrix[self.posX + 1][self.posY + 2].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX + 1, self.posY + 2))
    if self.posX + 2 <= 7:
      if self.posY - 1 >= 0:
        if(board.matrix[self.posX + 2][self.posY - 1] == None
        or (not board.matrix[self.posX + 2][self.posY - 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX + 2, self.posY - 1))
      if self.posY + 1 <= 7:
        if(board.matrix[self.posX + 2][self.posY + 1] == None
        or (not board.matrix[self.posX + 2][self.posY + 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX + 2, self.posY + 1))
    return available

  def is_illegal(self, startX, startY, endX, endY, board):
    if(board.matrix[endX][endY] == None
    or (not board.matrix[endX][endY].color
    == self.color)):
      if(((startX - endX == 2) or (startX - endX == -2))
      and ((startY - endY == 1) or (startY - endY == -1))):
        return False
      elif(((startY - endY == 2) or (startY - endY == -2))
      and ((startX - endX == 1) or (startX - endX == -1))):
        return False
      else:
        return True
    else:
      return True







