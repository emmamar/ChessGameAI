import Piece
from Move import Move

class Pawn(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.material = 100
    if (self.color == "W"):
      self.string_rep = "PW"
    else:
      self.string_rep = "PB"
    if(self.color == "B"):
      self.table = [0,   0,   0,   0,   0,   0,  0,  0,
                   50, 50,  50,  50,  50,  50, 50, 50,
                   10, 10,  20,  30,  30,  20, 10, 10,
                    5,   5,  10,  27,  27,  10,  5,  5,
                    0,   0,   0,  25,  25,   0,  0,  0,
                    5,  -5, -10,   0,   0, -10, -5,  5,
                    5,  10,  10, -25, -25,  10, 10,  5,
                    0,   0,   0,   0,   0,   0,  0,  0]
      
    else:
      self.table = [0,   0,   0,   0,   0,   0,   0,   0,
                    5,  10,  10, -25, -25,  10,  10,   5,
                    5,  -5, -10,   0,   0, -10,  -5,   5,
                    0,   0,   0,  25,  25,   0,   0,   0,
                    5,   5,  10,  27,  27,  10,   5,   5,
                   10,  10,  20,  30,  30,  20,  10,  10,
                   50,  50,  50,  50,  50,  50,  50,  50,
                    0,   0,   0,   0,   0,   0,   0,   0]
    self.available_moves = None
    self.attacking = None
    self.refresh_on_change_squares = None
    
  def refresh_state(self, board):
    posX = self.posX
    posY = self.posY
    self.attacking = []
    self.available_moves = []
    self.refresh_on_change_squares = []
    
    if self.color == "B":
      if board.matrix[posX - 1][posY] == None:
        self.available_moves += [[Move(posX, posY, posX - 1, posY), self.table[(posX - 1)*8 + posY] - self.table[(posX)*8 + posY]]]
        if(posX == 6
        and board.matrix[posX - 2][posY] == None):
          self.available_moves += [[Move(posX, posY, posX - 2, posY),self.table[(posX - 2)*8 + posY] - self.table[(posX)*8 + posY]]]
        self.refresh_on_change_squares += [[posX - 2,posY]]
      self.refresh_on_change_squares += [[posX - 1,posY]]
      if(posY < 7 and
      (not board.matrix[posX - 1][posY + 1] == None
      and board.matrix[posX - 1][posY + 1].color == "W")):
        self.available_moves += [[Move(posX, posY, posX - 1, posY + 1), self.table[(posX - 1)*8 + posY + 1] - self.table[(posX)*8 + posY] + board.matrix[posX - 1][posY + 1].material]]
        self.attacking += [board.matrix[posX - 1][posY + 1].__class__.__name__]
      self.refresh_on_change_squares += [[posX - 1,posY + 1]]
      if(posY > 0 and
      (not board.matrix[posX - 1][posY - 1] == None
      and board.matrix[posX - 1][posY - 1].color == "W")):
        self.available_moves += [[Move(posX, posY, posX - 1, posY - 1), self.table[(posX - 1)*8 + posY - 1] - self.table[(posX)*8 + posY] + board.matrix[posX - 1][posY - 1].material]]
        self.attacking += [board.matrix[posX - 1][posY - 1].__class__.__name__]
      self.refresh_on_change_squares += [[posX - 1,posY - 1]]
    else:
      if board.matrix[posX + 1][posY] == None:
        self.available_moves += [[Move(posX, posY, posX + 1, posY), self.table[(posX + 1)*8 + posY] - self.table[(posX)*8 + posY]]]
        if(posX == 1
        and board.matrix[posX + 2][posY] == None):
          self.available_moves += [[Move(posX,posY, posX + 2, posY), self.table[(posX + 2)*8 + posY] - self.table[(posX)*8 + posY]]]
        self.refresh_on_change_squares += [[posX + 2,posY]]
      self.refresh_on_change_squares += [[posX + 1,posY]]
      if(posY < 7 and
      ((not board.matrix[posX + 1][posY + 1] == None)
      and board.matrix[posX + 1][posY + 1].color == "B")):
        self.available_moves += [[Move(posX, posY, posX + 1, posY + 1), self.table[(posX + 1)*8 + posY + 1] - self.table[(posX)*8 + posY] + board.matrix[posX + 1][posY + 1].material]]
        self.attacking += [board.matrix[posX + 1][posY + 1].__class__.__name__]
      self.refresh_on_change_squares += [[posX + 1,posY + 1]]
      if(posY > 0 and
      ((not board.matrix[posX + 1][posY - 1] == None)
      and board.matrix[posX + 1][posY - 1].color == "B")):
        self.available_moves += [[Move(posX, posY, posX + 1, posY - 1), self.table[(posX + 1)*8 + posY - 1] - self.table[(posX)*8 + posY] + board.matrix[posX + 1][posY - 1].material]]
        self.attacking += [board.matrix[posX + 1][posY - 1].__class__.__name__]    
      self.refresh_on_change_squares += [[posX + 1,posY - 1]]  
  
 




