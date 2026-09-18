class WordDictionary:
    def __init__(self):
        self.trie = {'*' : False}

    
    def addWord(self, word: str) -> None:
        n = self.trie
        
        
        for letter in word:
            if letter not in n:
                n[letter] = {'*' : False}
            
            
            n = n[letter]
        
        
        n['*'] = True
    
    
    def search_in_trie(self, trie, word, start_idx, end_idx):
        for i in range(start_idx, end_idx):
            if word[i] == '.':
                word_found = False
                
                
                for letter in trie:
                    if letter != '*':
                        word_found = word_found or self.search_in_trie(trie[letter], word, i + 1, end_idx)
                    
                    
                    if word_found:
                        break
                
                
                return word_found
            
            
            if word[i] not in trie:
                return False
            
            
            trie = trie[word[i]]
        
        
        return trie['*']
    
    
    def search(self, word: str) -> bool:
        return self.search_in_trie(self.trie, word, 0, len(word))