import Piece
from Move import Move

class Pawn(Piece.Piece):
  def __init__(self, c):
    self.color = c
   
  def get_available_moves_specific(self, board, px, py):
    posX = px
    posY = py
    available = list()
    if self.color == "B":
      if board.matrix[posX - 1][posY] == None:
        available.append(Move(posX, posY, posX - 1, posY))
        if(posX == 6
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
        if(posX == 1
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
  
 
  def is_illegal(self, startX, startY, endX, endY, board):
    if self.color == "B":
      if startY == endY: 
        if(startX - endX == 1 and (board.matrix[endX][endY] == None)):
          return False
        elif(startX - endX == 2
        and (board.matrix[endX][endY] == None)
        and (startX == 6)
        and (board.matrix[startX - 1][startY] == None)):
          return False
        else:
          return True
      elif(abs(startY - endY) == 1
      and startX - endX == 1
      and not board.matrix[endX][endY] == None
      and not board.matrix[endX][endY].color
      == self.color):
        return False
      else:
        return True
    else:
      
      if(startY == endY):
        
        if(endX - startX == 1 and (board.matrix[endX][endY] == None)):
          return False
        elif((endX - startX == 2)
        and (startX == 1)
        and (board.matrix[endX][endY] == None)
        and (board.matrix[startX + 1][startY] == None)):
          return False
        else:
          return True
      elif((abs(endY - startY) == 1)
      and (endX - startX == 1)
      and not (board.matrix[endX][endY] == None)
      and not (board.matrix[endX][endY].color
      == self.color)):
        return False
      else:
        return True

  def toString(self):
    if self.color == "W":
      return "PW"
    else:
      return "PB"
    


