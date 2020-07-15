# Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

class Solution:
    def findComplement(self, num: int) -> int:
        if num==1:
            return 0
        elif num==0:
            return 1
        else:
            i=0
            number=1
            while(number<=num):
                i=i+1
                number=2**i
            return number-num-1
            
       
