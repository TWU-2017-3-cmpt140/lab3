#****************************************************************
# CMPT 140 Lab #3
#
# The MazerRunner class definition
#
#****************************************************************
from csv import reader
class MazerRunner:
   """
   fields:
      currX - current X coorindate
      currY - current Y coordinate
      startX - starting X position (bottom left)
      startY - starting Y position (bottom left)
      endX - end X position (top right)
      endY - end Y position (top right)
      map - list of arrays;
            note: map[y][x] because csv was read row by row
   """

   #########################################################
   # Class initializer
   # this function creates a MazerRunner object
   #
   # input: mazeFname - name of a file specifying the maze
   def __init__(self, mazeFname):
      self.map = []
      with open(mazeFname, newline="\n") as csvfile:
         filereader = reader(csvfile,delimiter=",")
         for row in filereader:
            for i in range(0,len(row)):
               row[i]=int(row[i])
            self.map.append(row)
      # initial position
      self.startX = 1 # since border always width 1
      self.startY = len(self.map)-2
      self.endX = len(self.map)-2
      self.endY = 1 # since border always width 1
      # start mazer runner at position startX, startY
      self.currX = self.startX
      self.currY = self.startY

   ##########################################################
   # returns a string representation of this MazerRunner
   # instance
   #
   # returns: a string
   def __str__(self):
      return "x:"+str(self.currX)+", y="+str(self.currY)

   ##########################################################
   # indicates whether this MazerRunner instance has reached
   # the end of the maze
   #
   # returns: True if finished, False otherwise
   def isFinished(self):
      return self.currX==self.endX and self.currY==self.endY

   ##########################################################
   # indicates whether this MazerRunner instance can move up
   # or down by the number of steps indicated by the input
   # "step"
   # e.g. if a wall is in its way, it cannot move up
   #
   # inputs: step = number of steps to move up/down
   #         if step<0, means move up
   #         if step>0, means move down
   # returns: True if can move up, False otherwise
   def canMoveVertical(self,step):
      newY = self.currY+step
      if newY <= self.startY and newY >= self.endY:
         return self.map[newY][self.currX]!=0
      else:
         return False

   ###########################################################
   # indicates whether this MazerRunner instance can move up
   # by one step
   #
   # returns: True if can move up, False otherwise
   def canMoveUp(self):
      return self.canMoveVertical(-1)

   ###########################################################
   # indicates whether this MazeRunner instance can move down
   # by one step
   #
   # returns: True if can move up, False otherwise
   def canMoveDown(self):
      return self.canMoveVertical(1)

   ###########################################################
   # move vertically by the number of steps specified by the
   # input "step"
   #
   # inputs: step = number of step to move vertically
   #         if step<0, means move up
   #         if step>0, means move down
   def moveVertical(self,step):
      if self.canMoveVertical(step):
         self.currY = self.currY+step

   ###########################################################
   # move up by one step
   #
   def moveUp(self):
      self.moveVertical(-1)
      
   ###########################################################
   # move down by one step
   #
   def moveDown(self):
      self.moveVertical(1)

   ###########################################################
   # indicates whether this MazerRunner instance can move left
   # or right by the number of steps indicated by the input
   # "step"
   # e.g. if a wall is in its way, it cannot move up
   #
   # inputs: step = number of steps to move left/right
   #         if step<0, means move left
   #         if step>0, means move right
   # returns: True if can move up, False otherwise
   def canMoveHorizontal(self,step):
      newX = self.currX+step
      if newX >= self.startX and newX <= self.endX:
         return self.map[self.currY][newX]!=0
      else:
         return False

   ###########################################################
   # indicates whether this MazerRunner instance can move left
   # by one step
   #
   # returns: True if can move left, False otherwise
   def canMoveLeft(self):
      return self.canMoveHorizontal(-1)

   ###########################################################
   # indicates whether this MazerRunner instance can move right
   # by one step
   #
   # returns: True if can move right, False otherwise
   def canMoveRight(self):
      return self.canMoveHorizontal(1)

   ###########################################################
   # move horizontally by the number of steps specified by the
   # input "step"
   #
   # inputs: step = number of step to move horizontally
   #         if step<0, means move left
   #         if step>0, means move right
   def moveHorizontal(self,step):
      if self.canMoveHorizontal(step):
         self.currX = self.currX+step
         
   ###########################################################
   # move left by one step
   #
   def moveLeft(self):
      self.moveHorizontal(-1)

   ###########################################################
   # move right by one step
   #
   def moveRight(self):
      self.moveHorizontal(1)
   
if __name__ == '__main__':
   tr = MazerRunner("maze1505369241.7894154.csv")
   
