# Implement a trie with insert, search, and startsWith methods.

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ans=[]

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.ans.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.ans:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        
        """
        for ans1 in self.ans:
            if len(ans1)>=len(prefix):
                flag=0
                for i in range(0,len(prefix)):
                    if ans1[i]!=prefix[i]:
                        flag=1
                        break
                if flag==0:
                    return True
        return False




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
