
class Move:
  ''' a move can be defined with an algebraic notation or
  int notation. Move will throw a ValueError if arguments
  are not a valid move)'''

  def __init__(self, x1, y1, x2, y2, alg=""):
    if x1 == -1 or y1 == -1 or x2 == -1 or y2 == -1:
      if alg == "":
        raise ValueError("move needs a move")
      else:
        self.algebraic = alg
        move_from_alg_dic = {"a":0, "b":1, "c":2, "d":3, "e":4,
        "f":5, "g":6, "h":7}
        split = list(alg)
        if(int(split[1]) < 1 or int(split[1]) > 8 or
           int(split[3]) < 1 or int(split[3]) > 8 or
           split[0] not in move_from_alg_dic or
           split[2] not in move_from_alg_dic):
          raise ValueError("not valid move")
        else:
          self.startX = int(split[1]) - 1
          self.startY = move_from_alg_dic[split[0]]
          self.endX = int(split[3]) - 1
          self.endY = move_from_alg_dic[split[2]]
    else:
      if(x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7
      or x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7):
        raise ValueError("not valid move")
      else:
        self.startX = x1
        self.startY = y1
        self.endX = x2
        self.endY = y2
        self.algebraic = None

  def getalg(self):
    if(self.algebraic == None):
      alg_dic = {"0":"a", "1":"b", "2":"c",
      "3": "d", "4":"e", "5":"f", "6":"g", "7":"h"}
      self.algebraic = (alg_dic[str(self.startY)] + 
      str(self.startX + 1) + alg_dic[str(self.endY)] + 
      str(self.endX + 1))
    return self.algebraic

  def get_algebraic(self):
    return self.algebraic
  def to_string(self):
    return ("[" + str(self.startX) + ", " + str(self.startY) 
    + ", " + str(self.endX) + ", " + str(self.endY) + "]")
        
