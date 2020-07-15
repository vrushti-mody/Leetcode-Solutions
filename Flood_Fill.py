# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

# At the end, return the modified image.

class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        old_color = image[sr][sc]
        queue = [(sr, sc)]
        seen = set()
        tot_rows = len(image)
        tot_cols = len(image[0])
        while queue:
            nxt = []
            for x,y in queue:
                image[x][y] = newColor
                seen.add((x,y))
                
                if x and (x-1,y) not in seen and image[x-1][y] == old_color: 
                    nxt.append((x-1,y))
                if y and (x,y-1) not in seen and image[x][y-1] == old_color:
                    nxt.append((x, y-1))
                if x < tot_rows-1 and (x+1,y) not in seen and image[x+1][y] == old_color:
                    nxt.append((x+1, y))
                if y < tot_cols-1 and (x,y+1) not in seen and image[x][y+1] == old_color:
                    nxt.append((x,y+1))
            
            queue = nxt
        
        return image
                        
