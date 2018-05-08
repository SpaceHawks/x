#
# Pathfinding Class
#
import math
#
class Pathfinding:


    def __init__(self):
        self.isForward = True
        self.r = 0.0  # radius of robot
        self.rX = 0.0  # x-coordinate of robot
        self.rY = 0.0  # y-coordinate of robot

        self.obstacles = [[0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0]]  # holds upto 5 self.obstacles

        self.numPivots = 0  # num of relevant self.obstacles
        self.pivots = [[0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0]]  # works with only 2 self.obstacles at any time

        self.dirr = 1
        self.dest = 1

        self.xA = 0.0
        self.yA = 0.0
        self.xB = 0.0
        self.yB = 0.0
        self.x1 = 0.0
        self.y1 = 0.0
        self.x2 = 0.0
        self.y2 = 0.0
        self.x3 = 0.0
        self.y3 = 0.0


    def setNumPivots(self, num):
        self.numPivots = num


    def setDest(self, f):
        self.isForward = f


    def setLoc(self, x, y):
        self.rX = x
        self.rY = y


    def setObstacles(self, xA, yA, xB, yB):
        self.pivots[0][0] = xA
        self.pivots[0][1] = yA
        self.pivots[1][0] = xB
        self.pivots[1][1] = yB


    def moveStraight(self):  # moves robot forward/backward 30 cm
        if (self.isForward == True):
            self.dest = 1
            self.x1 = self.rX + 100
            self.y1 = self.rY
            self.x2 = self.rX + 200
            self.y2 = self.rY
            self.x3 = self.rX + 300
            self.y3 = self.rY
        else:
            self.dest = -1
            self.x1 = self.rX - 100
            self.y1 = self.rY
            self.x2 = self.rX - 200
            self.y2 = self.rY
            self.x3 = self.rX - 300
            self.y3 = self.rY


    def pathA(self, num):  # if self.numPivots == 1
        if (self.isForward == True):
            self.dest = 1
        else:
            self.dest = -1
        if (num == 1):
            self.xA = self.pivots[0][0]
            self.yA = self.pivots[0][1]
            if (self.yA > 0.0):
                self.dirr = -1
            else:
                self.dirr = 1
        if (num == 2):
            if ((self.pivots[0][1] + self.pivots[1][1]) / 2 > 0):
                self.dirr = -1
            else:
                self.dirr = 1
            if (self.dirr == 1):
                if (self.pivots[0][1] > self.pivots[1][1]):
                    self.xA = self.pivots[0][0]
                    self.yA = self.pivots[0][1]
                    self.xB = self.pivots[1][0]
                    self.yB = self.pivots[1][1]
                else:
                    self.xA = self.pivots[1][0]
                    self.yA = self.pivots[1][1]
                    self.xB = self.pivots[0][0]
                    self.yB = self.pivots[0][1]
            else:
                if (self.pivots[0][1] > self.pivots[1][1]):
                    self.xA = self.pivots[1][0]
                    self.yA = self.pivots[1][1]
                    self.xB = self.pivots[0][0]
                    self.yB = self.pivots[0][1]
                else:
                    self.xA = self.pivots[0][0]
                    self.yA = self.pivots[0][1]
                    self.xB = self.pivots[1][0]
                    self.yB = self.pivots[1][1]
        self.x3 = self.xA
        self.y3 = self.yA + self.dirr * (self.r + 400)
        self.x2 = self.xA - self.dest * (self.r + 400) * 2 / 3
        self.y2 = self.y3
        self.x1 = self.xA - self.dest * (self.r + 400)
        self.y1 = self.y3 - self.dirr * (self.r + 400) / 3


    def pathB(self):  # if self.numPivots == 2
        self.xA = self.pivots[0][0]
        self.yA = self.pivots[0][1]
        self.xB = self.pivots[1][0]
        self.yB = self.pivots[1][1]
        width = math.sqrt(math.pow(self.xB - self.xA, 2) + math.pow(self.yB - self.yA, 2)) - self.pivots[0][2] - self.pivots[1][2]
        self.x1 = (self.xA + self.xB) / 2
        self.y1 = (self.yA + self.yB) / 2
        if (self.isForward == True):
            self.dest = 1
        else:
            self.dest = -1
        if (width > 2 * self.r):
            if (math.fabs(self.yA - self.yB) < 2 * self.r):
                if (self.dest * (self.xA - self.xB) < 0.0):
                    self.xA = self.pivots[1][0]
                    self.yA = self.pivots[1][1]
                    self.xB = self.pivots[0][0]
                    self.yB = self.pivots[0][1]
                if ((self.yA - self.yB) > 0.0):
                    self.dirr = -1
                else:
                    self.dirr = 1
                self.x2 = self.x1
                self.y2 = self.y1
                if (self.dest == self.dirr):
                    self.x1 = self.x2 - self.dest * 300
                    self.y1 = self.y2 - self.dest * 300
                else:
                    self.x1 = self.x2 + self.dirr * 300
                    self.y1 = self.y2 + self.dest * 300
                self.x3 = self.xA
                self.y3 = self.yA + self.dirr * (self.r + 400)
            else:
                self.x2 = self.x1
                self.y2 = self.y1
                self.x1 = self.x2 - self.dest * 200
                self.y3 = self.y2
                self.x3 = self.x2 + self.dest * 200
        else:
            self.pathA(2)  # treat the two self.obstacles as a single big one


    def setData(self, isForward, robotLoc, numPivots, obstacles):
        self.isForward = isForward
        self.rX = robotLoc[0]
        self.rY = robotLoc[1]
        self.numPivots = numPivots
        self.pivots = obstacles
        # pivots = closet 2 obstacles
        pass


    def getData(self): # Returns path of 3 points to move to
        if (self.numPivots == 0):
            self.moveStraight()
        if (self.numPivots == 1):
            self.pathA(1)
        if (self.numPivots == 2):
            self.pathB()
        else:
            pass
        return [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)]

#
# End Pathfinding
#