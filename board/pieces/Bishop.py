import Piece
from Move import Move

class Bishop(Piece.Piece):

<<<<<<< HEAD
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.material = 500
    if (self.color == "W"):
      self.string_rep = "BW"
    else:
      self.string_rep = "BB"
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
      
    self.available_moves = None
    self.attacking = None
    self.refresh_on_change_squares = None
        
        
  def refresh_state(self, board):
    self.available_moves = []
    self.attacking = []
    self.refresh_on_change_squares = []
    
    for i in xrange(1, 8 - self.posX):
      if self.posY + i <= 7:
        if(board.matrix[self.posX + i][self.posY + i] == None):
          self.available_moves += [[Move(self.posX,self.posY,self.posX + i, self.posY + i), self.table[(self.posX + i)*8 + self.posY + i] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + i][self.posY + i].color == self.color):
          self.available_moves += [[Move(self.posX,self.posY,self.posX + i, self.posY + i), self.table[(self.posX + i)*8 + self.posY + i] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + i][self.posY + i].material]]
          self.attacking += [board.matrix[self.posX + i][self.posY + i]]
        self.refresh_on_change_squares += [[self.posX + i, self.posY + i]]
        if (not board.matrix[self.posX + i][self.posY + i] == None):
          break
    for i in xrange(1, 8 - self.posX):
      if self.posY - i >= 0:
        if(board.matrix[self.posX + i][self.posY -i] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + i, self.posY - i), self.table[(self.posX + i)*8 + self.posY - i] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + i][self.posY - i].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + i, self.posY - i), self.table[(self.posX + i)*8 + self.posY - i] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + i][self.posY -i].material]]
          self.attacking += [board.matrix[self.posX + i][self.posY -i]]
        self.refresh_on_change_squares += [[self.posX + i,self.posY -i]]
        if (not board.matrix[self.posX + i][self.posY - i] == None):
          break
    for i in xrange(1, self.posX + 1):
      if self.posY + i <= 7:
        if(board.matrix[self.posX - i][self.posY + i] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - i, self.posY + i), self.table[(self.posX - i)*8 + self.posY + i] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - i][self.posY + i].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - i, self.posY + i), self.table[(self.posX - i)*8 + self.posY + i] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - i][self.posY + i].material]]
          self.attacking += [board.matrix[self.posX - i][self.posY + i]]
        self.refresh_on_change_squares += [[self.posX - i,self.posY + i]]
        if (not board.matrix[self.posX - i][self.posY + i] == None):
          break
    for i in xrange(1, self.posX + 1):
      if self.posY - i >= 0:
        if(board.matrix[self.posX - i][self.posY - i] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - i, self.posY - i), self.table[(self.posX - i)*8 + self.posY - i] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - i][self.posY - i].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - i, self.posY - i), self.table[(self.posX - i)*8 + self.posY - i] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - i][self.posY - i].material]]
          self.attacking += [board.matrix[self.posX - i][self.posY - i]]
        self.refresh_on_change_squares += [[self.posX - i,self.posY - i]]
        if (not board.matrix[self.posX - i][self.posY - i] == None):
          break
=======
  def __init__(self, c):
    self.color = c
        
  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()

    for i in range(1, 7 - posX):
      if posY + i <= 7:
        if(board.matrix[posX + i][posY + i] == None or not
          board.matrix[posX + i][posY + i].color == self.color):
          available.append(Move(posX,posY,posX + i, posY + i))
        if not board.matrix[posX + i][posY + i] == None:
          break
    for i in range(1, 7 - posX):
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
  def is_illegal(self, move, board):
    if abs(move.startX - move.endX) == abs(move.startY - 
      move.endY):
      length_X = move.startX - move.endX
      length_Y = move.startY - move.endY
      for i in range(1, abs(length_X)):
        if length_X < 0:
          if length_Y < 0:
            if not (board.matrix[move.startX + i][move.startY + i]
            == None):
              return True
          else:
            if not (board.matrix[move.startX + i][move.startY - i]
            == None):
              return True
        elif length_X > 0:
          if length_Y < 0:
            if not (board.matrix[move.startX - i][move.startY + i]
            == None):
              return True
          else:
            if not (board.matrix[move.startX - i][move.startY - i]
            == None):
              return True
      if(not board.matrix[move.startX - length_X]
      [move.startY - length_Y] == None):
        if(board.matrix[move.endX]
        [move.endY].color == self.color):
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


>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4
