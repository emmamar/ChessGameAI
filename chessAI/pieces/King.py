import Piece
from Move import Move

class King(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.material = 5000
    if (self.color == "W"):
      self.string_rep = "KW"
    else:
      self.string_rep = "KB"
    if (self.color == "B"):
      self.table = [-30, -40, -40, -50, -50, -40, -40, -30,
                    -30, -40, -40, -50, -50, -40, -40, -30,
                    -30, -40, -40, -50, -50, -40, -40, -30,
                    -30, -40, -40, -50, -50, -40, -40, -30,
                    -20, -30, -30, -40, -40, -30, -30, -20,
                    -10, -20, -20, -20, -20, -20, -20, -10,
                     20,  20,   0,   0,   0,   0,  20,  20,
                     20,  30,  10,   0,   0,  10,  30,  20]
    else:
      self.table = [20,  30,  10,   0,   0,  10,  30,  20,
                    20,  20,   0,   0,   0,   0,  20,  20,
                   -10, -20, -20, -20, -20, -20, -20, -10,
                   -20, -30, -30, -40, -40, -30, -30, -20,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30]

  def get_available_moves_specific(self, board):
    available = list()
    if self.posX < 7:
      if(board.matrix[self.posX + 1][self.posY] == None
      or (not board.matrix[self.posX + 1][self.posY].color == self.color)):
        available.append(Move(self.posX, self.posY, self.posX + 1, self.posY))
      if self.posY > 0:
        if(board.matrix[self.posX + 1][self.posY - 1] == None
        or (not board.matrix[self.posX + 1][self.posY - 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX + 1, self.posY - 1))
      if self.posY < 7:
        if(board.matrix[self.posX + 1][self.posY + 1] == None
        or (not board.matrix[self.posX + 1][self.posY + 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX + 1, self.posY + 1))
    if self.posX > 0:
      if(board.matrix[self.posX - 1][self.posY] == None
      or (not board.matrix[self.posX - 1][self.posY].color == self.color)):
        available.append(Move(self.posX, self.posY, self.posX - 1, self.posY))
      if self.posY > 0:
        if(board.matrix[self.posX - 1][self.posY - 1] == None
        or (not board.matrix[self.posX - 1][self.posY -1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX - 1, self.posY - 1))
      if self.posY < 7:
        if(board.matrix[self.posX - 1][self.posY + 1] == None
        or (not board.matrix[self.posX - 1][self.posY + 1].color == self.color)):
          available.append(Move(self.posX, self.posY, self.posX - 1, self.posY + 1))
    if self.posY < 7:
      if(board.matrix[self.posX][self.posY + 1] == None
      or (not board.matrix[self.posX][self.posY + 1].color == self.color)):
        available.append(Move(self.posX, self.posY, self.posX, self.posY + 1))
    if self.posY > 0:
      if(board.matrix[self.posX][self.posY - 1] == None
      or (not board.matrix[self.posX][self.posY - 1].color == self.color)):
        available.append(Move(self.posX, self.posY, self.posX, self.posY - 1))
    if(self.first_move):
      if(self.color == "B"):
        if(self.posX == 7 and self.posY == 4):
          if(board.matrix[7][0].__class__.__name__ == "Castle"):      
            if(board.matrix[7][0].first_move
            and board.matrix[7][1] == None
            and board.matrix[7][2] == None
            and board.matrix[7][3] == None):
              available.append(Move(self.posX, self.posY, self.posX, self.posY - 2))
          if(board.matrix[7][7].__class__.__name__ == "Castle"):
            if(board.matrix[7][7].first_move
            and board.matrix[7][6] == None
            and board.matrix[7][5] == None):
              available.append(Move(self.posX, self.posY, self.posX, self.posY + 2))
      else:
        if(self.posX == 0 and self.posY == 4): 
          if(board.matrix[0][0].__class__.__name__ == "Castle"):
            if(board.matrix[0][0].first_move
            and board.matrix[0][1] == None
            and board.matrix[0][2] == None
            and board.matrix[0][3] == None):
              available.append(Move(self.posX, self.posY, self.posX, self.posY - 2))
          if(board.matrix[0][7].__class__.__name__ == "Castle"):
            if(board.matrix[0][7].first_move
            and board.matrix[0][6] == None
            and board.matrix[0][5] == None):
              available.append(Move(self.posX, self.posY, self.posX, self.posY + 2))       
    return available

  def is_illegal(self, startX, startY, endX, endY, board):
    if(((((startX - endX <= 1) and (startX - endX >= -1))
    and ((startY - endY == 1) or (startY - endY == -1)))
    or ((startX - endX == 1) or (startX - endX == -1)
    and ((startY - endY <= 1) and (startY - endY >= -1))))
    and ((board.matrix[endX][endY] == None
    or not board.matrix[endX][endY].color == self.color))):
      return False
    else:
      return True

