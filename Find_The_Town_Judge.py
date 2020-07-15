# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N==1:
            return 1
        dic={}
        for i in range (1, N+1):
            dic[i]=0
     
        n=N-1
        li=[]
        ans=-1
        for i in range(0,len(trust)):
            dic[trust[i][1]]= dic[trust[i][1]]+1
            li.append(trust[i][0])
            if dic[trust[i][1]]== n:
                ans=trust[i][1]
    
        if ans in li:
            return -1
        else:
            return ans
      
