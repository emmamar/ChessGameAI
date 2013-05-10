import Piece
from Move import Move

class King(Piece.Piece):
<<<<<<< HEAD
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.material = 999
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
      self.table_end = [-50, -40, -30, -20, -20, -30, -40, -50,
                    -30, -30,   0,   0,   0,   0, -30, -30,
                    -30, -10,  20,  30,  30,  20, -10, -30,
                    -30, -10,  30,  40,  40,  30, -10, -30,
                    -30, -10,  30,  40,  40,  30, -10, -30,
                    -30, -10,  20,  30,  30,  20, -10, -30,
                    -30, -20, -10,   0,   0, -10, -20, -30,
                    -50, -30, -30, -30, -30, -30, -30, -50]
      
    else:
      self.table = [20,  30,  10,   0,   0,  10,  30,  20,
                    20,  20,   0,   0,   0,   0,  20,  20,
                   -10, -20, -20, -20, -20, -20, -20, -10,
                   -20, -30, -30, -40, -40, -30, -30, -20,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30,
                   -30, -40, -40, -50, -50, -40, -40, -30]
      self.table_end = [-50, -40, -30, -20, -20, -30, -40, -50,
                    -30, -20, -10,   0,   0, -10, -20, -30,
                    -30, -10,  20,  30,  30,  20, -10, -30,
                    -30, -10,  30,  40,  40,  30, -10, -30,
                    -30, -10,  30,  40,  40,  30, -10, -30,
                    -30, -10,  20,  30,  30,  20, -10, -30,
                    -30, -30,   0,   0,   0,   0, -30, -30,
                    -50, -30, -30, -30, -30, -30, -30, -50]
    self.available_moves = None
    self.attacking = None
    self.refresh_on_change_squares = None
    
  def refresh_state(self, board):
    self.attacking = []   
    self.available_moves = []
    self.refresh_on_change_squares = []
    
    if self.posX < 7:
      if(board.matrix[self.posX + 1][self.posY] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY), self.table[(self.posX + 1)*8 + self.posY] - self.table[(self.posX)*8 + self.posY]]]
      elif(not board.matrix[self.posX + 1][self.posY].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY), self.table[(self.posX + 1)*8 + self.posY] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 1][self.posY].material]]
        self.attacking += [board.matrix[self.posX + 1][self.posY]]
      self.refresh_on_change_squares += [[self.posX + 1,self.posY]]
      if self.posY > 0:
        if(board.matrix[self.posX + 1][self.posY - 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY - 1), self.table[(self.posX + 1)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + 1][self.posY - 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY - 1), self.table[(self.posX + 1)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 1][self.posY - 1].material]]
          self.attacking += [board.matrix[self.posX + 1][self.posY - 1]]
        self.refresh_on_change_squares += [[self.posX + 1,self.posY - 1]]
      if self.posY < 7:
        if(board.matrix[self.posX + 1][self.posY + 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY + 1), self.table[(self.posX + 1)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + 1][self.posY + 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY + 1), self.table[(self.posX + 1)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 1][self.posY + 1].material]]
          self.attacking += [board.matrix[self.posX + 1][self.posY + 1]]
        self.refresh_on_change_squares += [[self.posX + 1,self.posY + 1]]
    if self.posX > 0:
      if(board.matrix[self.posX - 1][self.posY] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY), self.table[(self.posX - 1)*8 + self.posY] - self.table[(self.posX)*8 + self.posY]]]
      elif(not board.matrix[self.posX - 1][self.posY].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY), self.table[(self.posX - 1)*8 + self.posY] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 1][self.posY].material]]
        self.attacking += [board.matrix[self.posX - 1][self.posY]]
      self.refresh_on_change_squares += [[self.posX - 1,self.posY]]
      if self.posY > 0:
        if(board.matrix[self.posX - 1][self.posY - 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY - 1), self.table[(self.posX - 1)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - 1][self.posY -1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY - 1), self.table[(self.posX - 1)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 1][self.posY - 1].material]]
          self.attacking += [board.matrix[self.posX - 1][self.posY - 1]]
        self.refresh_on_change_squares += [[self.posX - 1,self.posY - 1]]
      if self.posY < 7:
        if(board.matrix[self.posX - 1][self.posY + 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY + 1), self.table[(self.posX - 1)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - 1][self.posY + 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY + 1), self.table[(self.posX - 1)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 1][self.posY + 1].material]]
          self.attacking += [board.matrix[self.posX - 1][self.posY + 1]]
        self.refresh_on_change_squares += [[self.posX - 1,self.posY + 1]]
    if self.posY < 7:
      if(board.matrix[self.posX][self.posY + 1] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY + 1), self.table[(self.posX)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY]]]
      elif(not board.matrix[self.posX][self.posY + 1].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY + 1), self.table[(self.posX)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX][self.posY + 1].material]]
        self.attacking += [board.matrix[self.posX][self.posY + 1]]
      self.refresh_on_change_squares += [[self.posX,self.posY + 1]]
    if self.posY > 0:
      if(board.matrix[self.posX][self.posY - 1] == None):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY - 1), self.table[(self.posX)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY]]]
      elif(not board.matrix[self.posX][self.posY - 1].color == self.color):
        self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY - 1), self.table[(self.posX)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX][self.posY - 1].material]]
        self.attacking += [board.matrix[self.posX][self.posY - 1]]
      self.refresh_on_change_squares += [[self.posX,self.posY - 1]]
        
    if(self.first_move):
      if(self.color == "B"):
        if(self.posX == 7 and self.posY == 4):
          if(board.matrix[7][0].__class__.__name__ == "Castle"):      
            if(board.matrix[7][0].first_move
            and board.matrix[7][1] == None
            and board.matrix[7][2] == None
            and board.matrix[7][3] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece( [Move(self.posX, self.posY, self.posX, self.posY - 1), 0] )
                if(not board.is_check(self.color)):
                  self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY - 2), 50]]
                board.undo()'''
           
          if(board.matrix[7][7].__class__.__name__ == "Castle"):
            if(board.matrix[7][7].first_move
            and board.matrix[7][6] == None
            and board.matrix[7][5] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece( [Move(self.posX, self.posY, self.posX, self.posY - 1), 0] )
                if(not board.is_check(self.color)):
                  self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY + 2), 50]]
                board.undo()'''
      else:
        if(self.posX == 0 and self.posY == 4): 
          if(board.matrix[0][0].__class__.__name__ == "Castle"):
            if(board.matrix[0][0].first_move
            and board.matrix[0][1] == None
            and board.matrix[0][2] == None
            and board.matrix[0][3] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece( [Move(self.posX, self.posY, self.posX, self.posY - 1), 0] )
                if(not board.is_check(self.color)):
                  self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY - 2), 50]]
                board.undo()'''
          if(board.matrix[0][7].__class__.__name__ == "Castle"):
            if(board.matrix[0][7].first_move
            and board.matrix[0][6] == None
            and board.matrix[0][5] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece( [Move(self.posX, self.posY, self.posX, self.posY - 1), 0] )
                if(not board.is_check(self.color)):
                  self.available_moves += [[Move(self.posX, self.posY, self.posX, self.posY + 2), 50]]
                board.undo()'''

=======
  def __init__(self, c):
    self.color = c

  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()

    if posX < 7:
      if(board.matrix[posX + 1][posY] == None
      or not board.matrix[posX + 1][posY].color == self.color):
        available.append(Move(posX, posY, posX + 1, posY))
      if posY > 0:
        if(board.matrix[posX + 1][posY - 1] == None or not
          board.matrix[posX + 1][posY - 1].color == self.color):
          available.append(Move(posX, posY, posX + 1, posY - 1))
      if posY < 7:
        if(board.matrix[posX + 1][posY + 1] == None or not
          board.matrix[posX + 1][posY + 1].color == self.color):
          available.append(Move(posX, posY, posX + 1, posY + 1))
    if posX > 0:
      if(board.matrix[posX - 1][posY] == None
      or not board.matrix[posX - 1][posY].color == self.color):
        available.append(Move(posX, posY, posX - 1, posY))
      if posY > 0:
        if(board.matrix[posX - 1][posY -1] == None or not
        board.matrix[posX - 1][posY -1].color == self.color):
          available.append(Move(posX, posY, posX - 1, posY - 1))
      if posY < 7:
        if(board.matrix[posX - 1][posY + 1] == None or not
          board.matrix[posX - 1][posY + 1].color == self.color):
          available.append(Move(posX, posY, posX - 1, posY + 1))
    if posY < 7:
      if(board.matrix[posX][posY + 1] == None or not
        board.matrix[posX][posY + 1].color == self.color):
        available.append(Move(posX, posY, posX, posY + 1))
    if posY > 0:
      if(board.matrix[posX][posY - 1] == None or not
        board.matrix[posX][posY - 1].color == self.color):
        available.append(Move(posX, posY, posX, posY - 1))
    return available

  def is_illegal(self, move, board):
    if(((abs(move.startX - move.endX) <= 1
    and abs(move.startY - move.endY) == 1)
    or (abs(move.startX - move.endX) == 1
    and abs(move.startY - move.endY <= 1)))
    and (board.matrix[move.endX][move.endY] == None
    or not board.matrix[move.endX][move.endY].color
    == self.color)):
      return False
    else:
      return True

  def toString(self):
    if self.color == "W":
      return "KW"
    else:
      return "KB"
>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4
