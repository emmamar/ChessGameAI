import Piece
from Move import Move

class Pawn(Piece.Piece):
<<<<<<< HEAD
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
        self.attacking += [board.matrix[posX - 1][posY + 1]]
      self.refresh_on_change_squares += [[posX - 1,posY + 1]]
      if(posY > 0 and
      (not board.matrix[posX - 1][posY - 1] == None
      and board.matrix[posX - 1][posY - 1].color == "W")):
        self.available_moves += [[Move(posX, posY, posX - 1, posY - 1), self.table[(posX - 1)*8 + posY - 1] - self.table[(posX)*8 + posY] + board.matrix[posX - 1][posY - 1].material]]
        self.attacking += [board.matrix[posX - 1][posY - 1]]
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
        self.attacking += [board.matrix[posX + 1][posY + 1]]
      self.refresh_on_change_squares += [[posX + 1,posY + 1]]
      if(posY > 0 and
      ((not board.matrix[posX + 1][posY - 1] == None)
      and board.matrix[posX + 1][posY - 1].color == "B")):
        self.available_moves += [[Move(posX, posY, posX + 1, posY - 1), self.table[(posX + 1)*8 + posY - 1] - self.table[(posX)*8 + posY] + board.matrix[posX + 1][posY - 1].material]]
        self.attacking += [board.matrix[posX + 1][posY - 1]]    
      self.refresh_on_change_squares += [[posX + 1,posY - 1]]  
  
 


=======
  def __init__(self, c):
    self.color = c
    self.first_move = True
   
  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()
    if self.color == "B":
      if board.matrix[posX - 1][posY] == None:
        available.append(Move(posX, posY, posX - 1, posY))
        if(self.first_move
        and board.matrix[posX - 2][posY] == None):
          available.append(Move(posX, posY, posX - 2, posY))
      if(posY < 7 and
      (not board.matrix[posX - 1][posY + 1] == None
      and board.matrix[posX - 1][posY + 1].color == "W")):
        available.append(Move(posX, posY, posX - 1, posY + 1))
      if(posY > 0 and
      (not board.matrix[posX - 1][posY - 1] == None
      and board.matrix[posX - 1][posY - 1].color == "W")):
        available.append(Move(posX, posY, posX - 1, posY - 1))
    else:
      if board.matrix[posX + 1][posY] == None:
        available.append(Move(posX, posY, posX + 1, posY))
        if(self.first_move
        and board.matrix[posX + 2][posY] == None):
          available.append(Move(posX, posY, posX + 2, posY))
      if(posY < 7 and
      (not board.matrix[posX + 1][posY + 1] == None
      and board.matrix[posX + 1][posY + 1].color == "B")):
        available.append(Move(posX, posY, posX + 1, posY + 1))
      if(posY > 0 and
      (not board.matrix[posX + 1][posY - 1] == None
      and board.matrix[posX + 1][posY - 1].color == "B")):
        available.append(Move(posX, posY, posX + 1, posY - 1))
    return available          
  
  def is_illegal(self, move, board):
    if self.color == "B":
      if move.startY == move.endY:
        if(move.startX - move.endX == 1
        and board.matrix[move.endX][move.endY] == None):
          print "false 5"
          return False
        elif(move.startX - move.endX == 2
        and self.first_move == True
        and board.matrix[move.startX - 1][move.startY] == None
        and board.matrix[move.endX][move.endY] == None):
          print "false 6"
          return False
        else:
          return True
      elif(abs(move.startY - move.endY) == 1
      and move.startX - move.endX == 1
      and not board.matrix[move.endX][move.endY] == None
      and not board.matrix[move.endX][move.endY].color
      == self.color):
        print "false 7"
        return False
      else:
        return True
    else:
      if(move.startY == move.endY):
        if(move.endX - move.startX == 1
        and (board.matrix[move.endX][move.endY] == None)):
          return False
        elif((move.endX - move.startX == 2)
        and (self.first_move == True)
        and (board.matrix[move.startX + 1][move.startY] == None)
        and (board.matrix[move.endX][move.endY] == None)):
          print "false 8"
          return False
        else:
          return True
      elif((abs(move.endY - move.startY) == 1)
      and (move.endX - move.startX == 1)
      and not (board.matrix[move.endX][move.endY] == None)
      and not (board.matrix[move.endX][move.endY].color
      == self.color)):
        print "false 9"
        return False
      else:
        return True

  def toString(self):
    if self.color == "W":
      return "PW"
    else:
      return "PB"
    
>>>>>>> 179cf9c41a43cb1d35c3db4c4451e29e23c9abf4


