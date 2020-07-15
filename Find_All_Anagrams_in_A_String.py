# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        
        pdict={}
        sdict={}
        ans=[]
        for i in p:
            if i in pdict:
                pdict[i]=pdict[i]+1
            else:
                pdict[i]=1

        for i in range(0,len(p)):
            if s[i] in sdict:
                sdict[s[i]]=sdict[s[i]]+1
            else:
                sdict[s[i]]=1
        if sdict==pdict:
            ans.append(0)
        for i in range(1,len(s)-len(p)+1):
            sdict[s[i-1]]=sdict[s[i-1]]-1
            if sdict[s[i-1]]==0:
                del sdict[s[i-1]]
            if s[len(p)+i-1] in sdict:
                sdict[s[len(p)+i-1]]=sdict[s[len(p)+i-1]]+1
            else:
                sdict[s[len(p)+i-1]]=1
            
            if sdict==pdict:
                ans.append(i)
        return ans
