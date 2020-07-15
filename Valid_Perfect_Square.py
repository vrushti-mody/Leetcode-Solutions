# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num=num**0.5
        print( num)
        num=str(num)
        if num[len(num)-1]=='0':
            return True
        else:
            return False
