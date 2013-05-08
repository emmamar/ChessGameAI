import Piece
from Move import Move

class Knight(Piece.Piece):
  def __init__(self, c, px, py):
    self.color = c
    self.posX = px
    self.posY = py
    self.first_move = True
    self.material = 450
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

    self.available_moves = None
    self.attacking = None
    self.refresh_on_change_squares = None
    
  def refresh_state(self, board):
    self.available_moves = []
    self.attacking = []   
    self.refresh_on_change_squares = []
    
    if self.posX - 1 >= 0:
      if self.posY - 2 >= 0:
        if(board.matrix[self.posX - 1][self.posY - 2] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY - 2), self.table[(self.posX - 1)*8 + self.posY - 2] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - 1][self.posY - 2].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY - 2), self.table[(self.posX - 1)*8 + self.posY - 2] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 1][self.posY - 2].material]]
          self.attacking += [board.matrix[self.posX - 1][self.posY - 2]]
        self.refresh_on_change_squares += [[self.posX - 1,self.posY - 2]]
      if self.posY + 2 <= 7:
        if(board.matrix[self.posX - 1][self.posY + 2] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY + 2), self.table[(self.posX - 1)*8 + self.posY + 2] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - 1][self.posY + 2].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 1, self.posY + 2), self.table[(self.posX - 1)*8 + self.posY + 2] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 1][self.posY + 2].material]]
          self.attacking += [board.matrix[self.posX - 1][self.posY + 2]]
        self.refresh_on_change_squares += [[self.posX - 1,self.posY + 2]]
    if self.posX - 2 >= 0:
      if self.posY - 1 >= 0:
        if(board.matrix[self.posX - 2][self.posY - 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 2, self.posY - 1), self.table[(self.posX - 2)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - 2][self.posY - 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 2, self.posY - 1), self.table[(self.posX - 2)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 2][self.posY - 1].material]]
          self.attacking += [board.matrix[self.posX - 2][self.posY - 1]]
        self.refresh_on_change_squares += [[self.posX - 2,self.posY - 1]]
      if self.posY + 1 <= 7:
        if(board.matrix[self.posX - 2][self.posY + 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 2, self.posY + 1), self.table[(self.posX - 2)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX - 2][self.posY + 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX - 2, self.posY + 1), self.table[(self.posX - 2)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX - 2][self.posY + 1].material]]
          self.attacking += [board.matrix[self.posX - 2][self.posY + 1]]
        self.refresh_on_change_squares += [[self.posX - 2,self.posY + 1]]
    if self.posX + 1 <= 7:
      if self.posY - 2 >= 0:
        if(board.matrix[self.posX + 1][self.posY - 2] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY - 2), self.table[(self.posX + 1)*8 + self.posY - 2] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + 1][self.posY - 2].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY - 2), self.table[(self.posX + 1)*8 + self.posY - 2] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 1][self.posY - 2].material]]
          self.attacking += [board.matrix[self.posX + 1][self.posY - 2]]
        self.refresh_on_change_squares += [[self.posX + 1,self.posY - 2]]
      if self.posY + 2 <= 7:
        if(board.matrix[self.posX + 1][self.posY + 2] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY + 2), self.table[(self.posX + 1)*8 + self.posY + 2] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + 1][self.posY + 2].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 1, self.posY + 2), self.table[(self.posX + 1)*8 + self.posY + 2] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 1][self.posY + 2].material]]
          self.attacking += [board.matrix[self.posX + 1][self.posY + 2]]
        self.refresh_on_change_squares += [[self.posX + 1,self.posY + 2]]
    if self.posX + 2 <= 7:
      if self.posY - 1 >= 0:
        if(board.matrix[self.posX + 2][self.posY - 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 2, self.posY - 1), self.table[(self.posX + 2)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + 2][self.posY - 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 2, self.posY - 1), self.table[(self.posX + 2)*8 + self.posY - 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 2][self.posY - 1].material]]
          self.attacking += [board.matrix[self.posX + 2][self.posY - 1]]
        self.refresh_on_change_squares += [[self.posX + 2,self.posY - 1]]
      if self.posY + 1 <= 7:
        if(board.matrix[self.posX + 2][self.posY + 1] == None):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 2, self.posY + 1), self.table[(self.posX + 2)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY]]]
        elif(not board.matrix[self.posX + 2][self.posY + 1].color == self.color):
          self.available_moves += [[Move(self.posX, self.posY, self.posX + 2, self.posY + 1), self.table[(self.posX + 2)*8 + self.posY + 1] - self.table[(self.posX)*8 + self.posY] + board.matrix[self.posX + 2][self.posY + 1].material]]
          self.attacking += [board.matrix[self.posX + 2][self.posY + 1]]
        self.refresh_on_change_squares.append([self.posX + 2,self.posY + 1])


