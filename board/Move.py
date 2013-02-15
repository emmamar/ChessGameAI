

class Move:

  def __init__(self, x1, y1, x2, y2):
    self.startX = x1
    self.startY = y1
    self.endX = x2
    self.endY = y2

  def getStartX(self):
    return startX
  def getStartY(self):
    return startY
  def getEndX(self):
    return endX
  def getEndY(self):
    return endY
  def return_algebraic(self):
    alg_dic = {"0":"a", "1":"b", "2":"c", "3": "d", "4":"e", 
    "5":"f", "6":"g", "7":"h"}
    algebraic = (alg_dic[str(self.startY)] + str(self.startX + 1) 
    + alg_dic[str(self.endY)] + str(self.endX + 1))
    return algebraic

  def toString(self):
    return ("[" + str(self.startX) + ", " + str(self.startY) 
    + ", " +str(self.endX) + ", " + str(self.endY) + "]")
        
