import Piece
from Move import Move

class Castle(Piece.Piece):
<<<<<<< HEAD
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.table = None
    self.material = 600
    if (self.color == "W"):
      self.string_rep = "CW"
    else:
      self.string_rep = "CB"
    self.table = [0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]
    
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
        self.available_moves += [[Move(self.posX, self.posY, self.posX + i, self.posY), 0]]
      elif(not board.matrix[self.posX + i][self.posY].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX + i, self.posY), board.matrix[self.posX + i][self.posY].material]]
        self.attacking += [board.matrix[self.posX + i][self.posY]]
      self.refresh_on_change_squares += [[self.posX + i,self.posY]]
      if (not board.matrix[self.posX + i][self.posY] == None):
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posX - i < 0:
        break
      if(board.matrix[self.posX - i][self.posY] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX - i, self.posY), 0]]
      elif(not board.matrix[self.posX - i][self.posY].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX - i, self.posY), board.matrix[self.posX - i][self.posY].material]]
        self.attacking += [board.matrix[self.posX - i][self.posY]]
      self.refresh_on_change_squares += [[self.posX - i,self.posY]]
      if (not board.matrix[self.posX - i][self.posY] == None):
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posY + i > 7:
        break
      if(board.matrix[self.posX][self.posY + i] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY + i), 0]]
      elif(not board.matrix[self.posX][self.posY + i].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY + i), board.matrix[self.posX][self.posY + i].material]]
        self.attacking += [board.matrix[self.posX][self.posY + i]]
      self.refresh_on_change_squares += [[self.posX,self.posY + i]]
      if (not board.matrix[self.posX][self.posY + i] == None):
        break
    for i in [1,2,3,4,5,6,7]:
      if self.posY - i < 0:
        break
      if(board.matrix[self.posX][self.posY - i] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY - i), 0]]
      elif(not board.matrix[self.posX][self.posY - i].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY - i), board.matrix[self.posX][self.posY - i].material]]
        self.attacking += [board.matrix[self.posX][self.posY - i]]
      self.refresh_on_change_squares += [[self.posX,self.posY - i]]
      if (not board.matrix[self.posX][self.posY - i] == None):
        break       

=======
  def __init__(self, c):
    self.color = c

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
  
  def is_illegal(self, move, board):
    if(abs(move.startX - move.endX) > 0
    and abs(move.startY - move.endY) == 0):
      length_of_move = move.startX - move.endX
      for i in range(1, abs(length_of_move)):
        if(length_of_move < 0):
          if(not board.matrix[move.startX + i][move.startY]
          == None):
            return True
        else:
          if(not board.matrix[move.startX - i][move.startY]
          == None):
            return True
      if(not board.matrix[move.startX - length_of_move]
      [move.startY] == None):
        if(board.matrix[move.startX - length_of_move]
        [move.startY].color == self.color):
          return True
        else:
          return False
      else:
        return False
    elif(abs(move.startX - move.endX) == 0
    and abs(move.startY - move.endY) > 0):
      length_of_move = move.startY - move.endY
      for i in range(1, abs(length_of_move)):
        if(length_of_move < 0):
          if(not board.matrix[move.startX][move.startY + i]
          == None):
            return True
        else:
          if(not board.matrix[move.startX][move.startY - i]
          == None):
            return True
      if(not board.matrix[move.startX]
      [move.startY - length_of_move] == None):
        if(board.matrix[move.startX]
        [move.startY - length_of_move].color == self.color):
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
>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4

