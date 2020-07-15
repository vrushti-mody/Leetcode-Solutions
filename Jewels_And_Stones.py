# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j=0
        i=0
        count=0
        while i<len(S):
            if j==len(J):
                j=0
                i=i+1
            elif S[i]==J[j]:
                i=i+1
                j=0
                count=count+1
            else:
                j=j+1
        return count
