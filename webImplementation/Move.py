

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
  

    def toString(self):
        return "[" + str(self.startX) +", " + str(self.startY) + ", " + str(self.endX) + ", " + str(self.endY) + "]"
