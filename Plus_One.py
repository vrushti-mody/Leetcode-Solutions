# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1]<9:
            digits[len(digits)-1]=digits[len(digits)-1]+1
        else:
            i=len(digits)-1
            while(digits[i]==9):    
                digits[i]=0
                i=i-1
            if i==-1:
                return [1]+digits
            else:
                digits[i]=digits[i]+1
        return digits
                    
