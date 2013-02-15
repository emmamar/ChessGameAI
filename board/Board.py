from pieces import Castle
from pieces import King
from pieces import Queen
from pieces import Bishop
from pieces import Knight
from pieces import Pawn

class Board:
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

  def createPiece(self, item):
    piece_map = {"00":None, "PB":Pawn.Pawn("B"), "KB":King.King("B"), 
    "QB":Queen.Queen("B"), "BB":Bishop.Bishop("B"), 
    "RB":Knight.Knight("B"), "CB":Castle.Castle("B"), "PW":Pawn.Pawn("W"), 
    "KW":King.King("W"), "QW":Queen.Queen("W"), "BW":Bishop.Bishop("W"), 
    "RW":Knight.Knight("W"), "CW":Castle.Castle("W")}
    return piece_map[item]

  def move_piece(self, move):
    self.matrix[move.endX][move.endY]=self.matrix[move.startX][move.startY]
    self.matrix[move.startX][move.startY] = None
        
  def save_board(self):
    f = open('/home/emma/Python/board/Board.txt', 'w')
    f.write(self.toString())

  def getMatrix(self):
    return matrix
    
  def getValueAt(self,x,y):
    if (x < 0 or x >= 8 or y < 0 or y >= 8):
      print "not in range"
    return matrix[x][y].toString()

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

  def is_check_mate(self):
    return True


