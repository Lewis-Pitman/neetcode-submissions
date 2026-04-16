class PrefixTree:

    class Node:
        def __init__(self, val: str, children: dict[Node] = None, end_of_word: bool = False):
            self.val = val
            self.children = children if children is not None else {}
            self.end_of_word = end_of_word

    def __init__(self):
        self.root = self.Node(val="0")

    def insert(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                new_node = self.Node(val=letter)
                curr.children[letter] = new_node
                curr = new_node
                
        
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for letter in prefix:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                return False
        
        return True