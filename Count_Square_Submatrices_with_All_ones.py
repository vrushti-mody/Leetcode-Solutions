# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
         # Initialize count variable 
        N=len(matrix)
        M= len(matrix[0])
        a=matrix
        count = 0

        for i in range(1, N): 
            for j in range(1, M): 

                # If a[i][j] is equal to 0 
                if (a[i][j] == 0): 
                    continue

                # Calculate number of 
                # square submatrices 
                # ending at (i, j) 
                a[i][j] = min([a[i - 1][j],  
                          a[i][j - 1], a[i - 1][j - 1]])+1

        # Calculate the sum of the array 
        for i in range(N): 
            for j in range(M): 
                count += a[i][j] 

        return count 
