class Node:
    def __init__(self,val):
        self.val=val
        self.is_end=False
        self.Next=[None]*(26)
class Trie:
    def __init__(self):
        #starting is a dummy start 
        self.head=Node(" ")
    def insert(self,word):
        curr=self.head
        for val in  word:
            idx=ord(val)-ord('a')
            if curr.Next[idx] is None:
                curr.Next[idx]=Node(val)
            curr=curr.Next[idx]
        #as we reached the end of the word 
        curr.is_end=True
    def check(self,word):
        #this check if the word is present or not 
        curr=self.head
        for val in word:
            idx=ord(val)-ord('a')
            if curr.Next[idx] is None:
                return False
            curr=curr.Next[idx]
        if curr.is_end:
            return True
        return False
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
      
        n=len(s)
        fans=[]
        t=Trie()
        for word in wordDict:
            t.insert(word)
       
        def dfs(idx,word,ans):
            nonlocal fans
            if idx==n:
                if word==[]:
                    fans.append(' '.join(ans))
                return 
            word.append(s[idx])
            sword=''.join(word)
            if t.check(sword):
                
                ans.append(sword)
                dfs(idx+1,[],ans)
                ans.pop()
            dfs(idx+1,word,ans)
        dfs(0,[],[])
        return fans