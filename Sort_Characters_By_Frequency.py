# Given a string, sort it in decreasing order based on the frequency of characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        
        dic=sorted(dic.items(), key=lambda x: x[1], reverse=True)
      
        k=""
        for i in range (0,len(dic)):
            k=k+(dic[i][0]*dic[i][1])
        return k
        
