class Trie:
    def __init__(self):
        self.root = {}        
    def insert(self, word: str) -> None:
        cur = self.root
        for ltr in word:
            cur = cur.setdefault(ltr, {})
        cur['_'] = 0
    def search(self, word: str) -> bool:
        cur = self.root
        for ltr in word:
            if ltr not in cur:
                return False
            cur = cur[ltr]
        return '_' in cur
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ltr in prefix:
            if ltr not in cur:
                return False
            cur = cur[ltr]
        return True