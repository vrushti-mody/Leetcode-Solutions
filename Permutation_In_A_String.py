# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        dict1={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        dict2={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for i in range(0,len(s1)):
            dict1[s1[i]]=dict1[s1[i]]+1
            dict2[s2[i]]=dict2[s2[i]]+1
            
        if dict1==dict2:
            return True
        
        for j in range(1,len(s2)-len(s1)+1):
            dict2[s2[j-1]]=dict2[s2[j-1]]-1
            dict2[s2[j+len(s1)-1]]=dict2[s2[j+len(s1)-1]]+1
           
            if dict1==dict2:
                return True
        return False
