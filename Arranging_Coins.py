#Arranging Coins

# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        ans= int((-1 + ((1+8*n)**(1/2)))//2)
        return ans
        
