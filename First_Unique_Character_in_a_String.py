# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        order = {}
        counts = {}
        for x in range(0,len(s)): 
            if s[x] in counts:
                
                counts[s[x]] += 1
            else:
                counts[s[x]] = 1 
                order[s[x]]=x
        for x in order:
            if counts[x] == 1:
                return order[x]
        return -1
