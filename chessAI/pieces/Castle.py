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
    if (self.color == "W"):
      self.string_rep = "CW"
    else:
      self.string_rep = "CB"
    
    self.available_moves = None
    self.attacking = None
    self.refresh_on_change_squares = None
    
  def refresh_state(self, board):
    self.attacking = []
    self.available_moves = []
    self.refresh_on_change_squares = []

    for i in [1,2,3,4,5,6,7]:
      if self.posX + i > 7:
        break
      if(board.matrix[self.posX + i][self.posY] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX + i, self.posY)]
      elif(not board.matrix[self.posX + i][self.posY].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX + i, self.posY)]
        self.attacking += [board.matrix[self.posX + i][self.posY]]
      self.refresh_on_change_squares += [[self.posX + i,self.posY]]
      if (not board.matrix[self.posX + i][self.posY] == None):
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posX - i < 0:
        break
      if(board.matrix[self.posX - i][self.posY] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX - i, self.posY)]
      elif(not board.matrix[self.posX - i][self.posY].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX - i, self.posY)]
        self.attacking += [board.matrix[self.posX - i][self.posY]]
      self.refresh_on_change_squares += [[self.posX - i,self.posY]]
      if (not board.matrix[self.posX - i][self.posY] == None):
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posY + i > 7:
        break
      if(board.matrix[self.posX][self.posY + i] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY + i)]
      elif(not board.matrix[self.posX][self.posY + i].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY + i)]
        self.attacking += [board.matrix[self.posX][self.posY + i]]
      self.refresh_on_change_squares += [[self.posX,self.posY + i]]
      if (not board.matrix[self.posX][self.posY + i] == None):
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posY - i < 0:
        break
      if(board.matrix[self.posX][self.posY - i] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY - i)]
      elif(not board.matrix[self.posX][self.posY - i].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY - i)]
        self.attacking += [board.matrix[self.posX][self.posY - i]]
      self.refresh_on_change_squares += [[self.posX,self.posY - i]]
      if (not board.matrix[self.posX][self.posY - i] == None):
        break       


