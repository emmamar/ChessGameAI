import Piece
from Move import Move

class Pawn(Piece.Piece):
  def __init__(self, c):
    self.color = c
    self.first_move = True
   
  def get_available_moves(self, board, px, py):
    posX = px
    posY = py
    available = list()
    if self.color == "B":
      if board.matrix[posX - 1][posY] == None:
        move_to_try = Move(posX, posY, posX - 1, posY)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
        if self.first_move and board.matrix[posX - 2][posY] == None:
          move_to_try = Move(posX, posY, posX - 2, posY)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
      if(posY < 7 and (not board.matrix[posX - 1][posY + 1] == None
      and board.matrix[posX - 1][posY + 1].color == "W")):
        move_to_try = Move(posX, posY, posX - 1, posY + 1)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
      if(posY > 0 and (not board.matrix[posX - 1][posY - 1] == None
      and board.matrix[posX - 1][posY - 1].color == "W")):
        move_to_try = Move(posX, posY, posX - 1, posY - 1)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
    else:
      if board.matrix[posX + 1][posY] == None:
        move_to_try = Move(posX, posY, posX + 1, posY)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
        if self.first_move and board.matrix[posX + 2][posY] == None:
          move_to_try = Move(posX, posY, posX + 2, posY)
          if self.check_if_not_check(board,move_to_try):
            available.append(move_to_try)
      if(posY < 7 and (not board.matrix[posX + 1][posY + 1] == None
      and board.matrix[posX + 1][posY + 1].color == "B")):
        move_to_try = Move(posX, posY, posX + 1, posY + 1)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
      if(posY > 0 and (not board.matrix[posX + 1][posY - 1] == None
      and board.matrix[posX + 1][posY - 1].color == "B")):
        move_to_try = Move(posX, posY, posX + 1, posY - 1)
        if self.check_if_not_check(board,move_to_try):
          available.append(move_to_try)
    return available          
  
  def is_illegal(self, move, board):
    if self.color == "B":
      if move.startY == move.endY:
        if(move.startX - move.endX == 1
        and board.matrix[move.endX][move.endY] == None):
          return False
        elif(move.startX - move.endX == 2
        and self.first_move == True
        and board.matrix[move.startX - 1][move.startY] == None
        and board.matrix[move.endX][move.endY] == None):
          return False
      elif(abs(move.startY - move.endY) == 1
      and move.startX - move.endX == 1
      and not board.matrix[move.endX][move.endY] == None
      and not board.matrix[move.endX][move.endY].color
      == self.color):
        return False
      else:
        return True
    else:
      if move.startY == move.endY:
        if(move.endX - move.startX == 1
        and board.matrix[move.endX][move.endY] == None):
          return False
        elif(move.endX - move.startX == 2
        and self.first_move == True
        and board.matrix[move.startX + 1][move.startY] == None
        and board.matrix[move.endX][move.endY] == None):
          return False
      elif(abs(move.endY - move.startY) == 1
      and move.endX - move.startX == 1
      and not board.matrix[move.endX][move.endY] == None
      and not board.matrix[move.endX][move.endY].color
      == self.color):
        return False
      else:
        return True

  def toString(self):
    if self.color == "W":
      return "PW"
    else:
      return "PB"
    


