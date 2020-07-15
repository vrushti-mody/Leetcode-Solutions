# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
        li=[]
        for i in range(0,len(num)):
            li.append(num[i])
            
        for j in range(0,k):
            i=0
            while i<len(li)-1 and int(li[i])<=int(li[i+1]):
                i=i+1
            li.pop(i)
        s=""
        for i in li:
            s=s+i
        s=int(s)
        return str(s)
