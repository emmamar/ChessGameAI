from pieces import Castle
from pieces import King
from pieces import Queen
from pieces import Bishop
from pieces import Knight
from pieces import Pawn
from Move import Move
import sys

'''this class creates a board object that stores information
about the current board configuration.'''

class Board:
  '''constructor: creates a matrix from the file Board.txt'''
  def __init__ (self):
    f = open('/home/emma/Python/board/Board.txt')
    self.matrix = list()
    i = 0
    for line in f:
      row_list = str.split(line)
      self.matrix.append(list())
      for item in row_list:
        self.matrix[i].append(self.createPiece(item))
      i += 1

  '''creates a specific piece object given its representation
  in the Board.txt file'''
  def createPiece(self, item):
    piece_map = {"00":None, "PB":Pawn.Pawn("B"),
    "KB":King.King("B"), "QB":Queen.Queen("B"),
    "BB":Bishop.Bishop("B"), "RB":Knight.Knight("B"),
    "CB":Castle.Castle("B"), "PW":Pawn.Pawn("W"),
    "KW":King.King("W"), "QW":Queen.Queen("W"),
    "BW":Bishop.Bishop("W"), "RW":Knight.Knight("W"),
    "CW":Castle.Castle("W")}
    return piece_map[item]


  '''moves a piece on the board given the move'''
  def try_move_piece(self, move):
    '''if(not self.is_illegal_move(move)):'''
    if(self.matrix[move.startX]
    [move.startY].__class__.__name__ == "Pawn"):
      self.matrix[move.startX][move.startY].first_move = False
    self.matrix[move.endX][move.endY] = (
    self.matrix[move.startX][move.startY])
    self.matrix[move.startX][move.startY] = None
    return True
    '''else:
    return False'''

  '''saves the current board configuration back to the Board.txt
  file'''
  def save_board(self):
    f = open('/home/emma/Python/board/BoardPlayed.txt', 'w')
    f.write(self.toString())

  '''returns the current board matrix configuration'''
  def getMatrix(self):
    return matrix
    
  '''returns the given piece at a position in the same
  representation as Board.txt'''
  def getValueAt(self,x,y):
    if (x < 0 or x >= 8 or y < 0 or y >= 8):
      print "not in range"
    return matrix[x][y].toString()

  '''returns the matrix in string form like in Board.txt'''
  def toString(self):
    board_string = ''
    for i in range(0,8):
      for j in range(0,8):
        if self.matrix[i][j] == None:
          board_string += "00" + ' '
        else:
          board_string += self.matrix[i][j].toString() + ' '
      board_string += '\n'
    return board_string

  '''determines wether the current board represents a check
  mate configuration'''
  def is_check_mate(self):
    return True

  '''determines wether the current board represents a check
  configuration'''
  def is_check(self, color):
    check = False
    for i in range(0,8):
      for j in range(0,8):
        if(self.matrix[i][j].__class__.__name__ == "King"
        and self.matrix[i][j].color == color):
          for k in range(0,8):
            for l in range(0,8):
              if not self.matrix[k][l] == None:
                if not self.matrix[k][l].color == color:
                  check = not self.matrix[k][l].is_illegal(
                    Move(k,i,l,j), self
                  )
                if check:
                  print Move(k,i,l,j).toString()
                  return check
    return check

  def is_illegal_move(self, move):
    return self.matrix[move.startX][move.startY].is_illegal(
      move,self
    )

