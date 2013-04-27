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
        self.available_moves += [Move(self.posX, self.posY, self.posX + 1, self.posY)]
      elif(not board.matrix[self.posX + 1][self.posY].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX + 1, self.posY)]
        self.attacking += [board.matrix[self.posX + 1][self.posY]]
      self.refresh_on_change_squares += [[self.posX + 1,self.posY]]
      if self.posY > 0:
        if(board.matrix[self.posX + 1][self.posY - 1] == None):
          self.available_moves += [Move(self.posX, self.posY, self.posX + 1, self.posY - 1)]
        elif(not board.matrix[self.posX + 1][self.posY - 1].color == self.color):
          self.available_moves += [Move(self.posX, self.posY, self.posX + 1, self.posY - 1)]
          self.attacking += [board.matrix[self.posX + 1][self.posY - 1]]
        self.refresh_on_change_squares += [[self.posX + 1,self.posY - 1]]
      if self.posY < 7:
        if(board.matrix[self.posX + 1][self.posY + 1] == None):
          self.available_moves += [Move(self.posX, self.posY, self.posX + 1, self.posY + 1)]
        elif(not board.matrix[self.posX + 1][self.posY + 1].color == self.color):
          self.available_moves += [Move(self.posX, self.posY, self.posX + 1, self.posY + 1)]
          self.attacking += [board.matrix[self.posX + 1][self.posY + 1]]
        self.refresh_on_change_squares += [[self.posX + 1,self.posY + 1]]
    if self.posX > 0:
      if(board.matrix[self.posX - 1][self.posY] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX - 1, self.posY)]
      elif(not board.matrix[self.posX - 1][self.posY].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX - 1, self.posY)]
        self.attacking += [board.matrix[self.posX - 1][self.posY]]
      self.refresh_on_change_squares += [[self.posX - 1,self.posY]]
      if self.posY > 0:
        if(board.matrix[self.posX - 1][self.posY - 1] == None):
          self.available_moves += [Move(self.posX, self.posY, self.posX - 1, self.posY - 1)]
        elif(not board.matrix[self.posX - 1][self.posY -1].color == self.color):
          self.available_moves += [Move(self.posX, self.posY, self.posX - 1, self.posY - 1)]
          self.attacking += [board.matrix[self.posX - 1][self.posY - 1]]
        self.refresh_on_change_squares += [[self.posX - 1,self.posY - 1]]
      if self.posY < 7:
        if(board.matrix[self.posX - 1][self.posY + 1] == None):
          self.available_moves += [Move(self.posX, self.posY, self.posX - 1, self.posY + 1)]
        elif(not board.matrix[self.posX - 1][self.posY + 1].color == self.color):
          self.available_moves += [Move(self.posX, self.posY, self.posX - 1, self.posY + 1)]
          self.attacking += [board.matrix[self.posX - 1][self.posY + 1]]
        self.refresh_on_change_squares += [[self.posX - 1,self.posY + 1]]
    if self.posY < 7:
      if(board.matrix[self.posX][self.posY + 1] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY + 1)]
      elif(not board.matrix[self.posX][self.posY + 1].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY + 1)]
        self.attacking += [board.matrix[self.posX][self.posY + 1]]
      self.refresh_on_change_squares += [[self.posX,self.posY + 1]]
    if self.posY > 0:
      if(board.matrix[self.posX][self.posY - 1] == None):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY - 1)]
      elif(not board.matrix[self.posX][self.posY - 1].color == self.color):
        self.available_moves += [Move(self.posX, self.posY, self.posX, self.posY - 1)]
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
                board.try_move_piece(Move(7,4,7,3))
                if(not board.is_check(self.color)):
                  board.undo()
                  available.append(Move(self.posX, self.posY, self.posX, self.posY - 2))
                else:
                  board.undo()  '''                
          if(board.matrix[7][7].__class__.__name__ == "Castle"):
            if(board.matrix[7][7].first_move
            and board.matrix[7][6] == None
            and board.matrix[7][5] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece(Move(7,4,7,5))
                if(not board.is_check(self.color)):
                  board.undo()
                  available.append(Move(self.posX, self.posY, self.posX, self.posY + 2))
                else:
                  board.undo() '''
              
      else:
        if(self.posX == 0 and self.posY == 4): 
          if(board.matrix[0][0].__class__.__name__ == "Castle"):
            if(board.matrix[0][0].first_move
            and board.matrix[0][1] == None
            and board.matrix[0][2] == None
            and board.matrix[0][3] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece(Move(0,4,0,3))
                if(not board.is_check(self.color)):
                  board.undo()
                  available.append(Move(self.posX, self.posY, self.posX, self.posY - 2))
                else:
                  board.undo() ''' 
          if(board.matrix[0][7].__class__.__name__ == "Castle"):
            if(board.matrix[0][7].first_move
            and board.matrix[0][6] == None
            and board.matrix[0][5] == None):
              pass
              '''if(not board.is_check(self.color)):
                board.try_move_piece(Move(0,4,0,5))
                if(not board.is_check(self.color)):
                  board.undo()
                  available.append(Move(self.posX, self.posY, self.posX, self.posY + 2))  
                else:
                  board.undo() '''

