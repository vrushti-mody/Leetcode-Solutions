#You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

#Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

#The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1):
                    if j+1>=len(grid[0]) or grid[i][j+1]==0 :
                        count=count+1
                    if (j-1<0 or grid[i][j-1]==0 ):
                        count=count+1
                    if( i+1>=len(grid) or grid[i+1][j]==0 ):
                        count=count+1
                    if (i-1<0 or grid[i-1][j]==0 ):
                        count=count+1
        return count
                    
