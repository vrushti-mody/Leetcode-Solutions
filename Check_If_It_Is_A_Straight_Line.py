# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        x2=coordinates[1][0]
        y2=coordinates[1][1]
        if (x1-x2!=0):
            m=(y1-y2)/(x1-x2)
            for i in range(2,len(coordinates)):
                x= coordinates[i][0]
                y= coordinates[i][1]
                if y-y1!=m*(x-x1):
                    return False
            return True
        else:
            for i in range(2,len(coordinates)):
                x= coordinates[i][0]
                
                if x!= x1:
                    return False
            return True
            
