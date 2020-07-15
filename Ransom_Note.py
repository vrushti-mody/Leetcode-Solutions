# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mag = { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,"k": 0, "l": 0, "m": 0, "n": 0, "o": 0,"p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0,"x": 0, "y": 0, "z": 0
            
}
        flag=0
        for i in magazine:
            mag[i]=mag[i]+1
        for i in ransomNote:
            mag[i]=mag[i]-1
            if(mag[i]<0):
                flag=1
                break
        if flag==0:
            return True
        else:
            return False
