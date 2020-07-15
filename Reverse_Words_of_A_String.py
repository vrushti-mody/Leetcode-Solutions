# Given an input string, reverse the string word by word.

class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        a=""
        for i in range(0,len(li)):
            if i==len(li)-1:
                a=a+li[len(li)-i-1]
            else:
                a=a+li[len(li)-i-1]+" "
        return (a)
