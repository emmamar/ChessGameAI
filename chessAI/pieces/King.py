import Piece
from Move import Move

class King(Piece.Piece):
  def __init__(self, c):
    self.color = c
    self.first_move = True

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
    if(self.first_move):
      if(self.color == "B"):
        if(posX == 7 and posY == 4):
          if(board.matrix[7][0].__class__.__name__ == "Castle"):      
            if(board.matrix[7][0].get_first_move()
            and board.matrix[7][1] == None
            and board.matrix[7][2] == None
            and board.matrix[7][3] == None):
              available.append(Move(posX, posY, posX, posY - 2))
          if(board.matrix[7][7].__class__.__name__ == "Castle"):
            if(board.matrix[7][7].get_first_move()
            and board.matrix[7][6] == None
            and board.matrix[7][5] == None):
              available.append(Move(posX, posY, posX, posY + 2))
      else:
        if(posX == 0 and posY == 4): 
          if(board.matrix[0][0].__class__.__name__ == "Castle"):
            if(board.matrix[0][0].get_first_move()
            and board.matrix[0][1] == None
            and board.matrix[0][2] == None
            and board.matrix[0][3] == None):
              available.append(Move(posX, posY, posX, posY - 2))
          if(board.matrix[0][7].__class__.__name__ == "Castle"):
            if(board.matrix[0][7].get_first_move()
            and board.matrix[0][6] == None
            and board.matrix[0][5] == None):
              available.append(Move(posX, posY, posX, posY + 2))       
    return available

  def get_first_move(self):
    return self.first_move
  
  def set_first(self, arg):
    self.first_move = arg


  def is_illegal(self, startX, startY, endX, endY, board):
    if(((abs(startX - endX) <= 1
    and abs(startY - endY) == 1)
    or (abs(startX - endX) == 1
    and abs(startY - endY <= 1)))
    and (board.matrix[endX][endY] == None
    or not board.matrix[endX][endY].color
    == self.color)):
      return False
    else:
      return True
  def toString(self):
    if self.color == "W":
      return "KW"
    else:
      return "KB"