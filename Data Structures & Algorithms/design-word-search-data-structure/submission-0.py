class WordDictionary:

    class Node:
        def __init__(
                self, 
                val: str, 
                children: dict["Node"] | None = None,
                end_of_word: bool = False
            ):
            self.val = val
            self.children = children if children is not None else {}
            self.end_of_word = end_of_word

    def __init__(self):
        self.root = self.Node("")

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = self.Node(char)
            curr = curr.children[char]

        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i in range(len(word) - 1):
            # Return early if no children
            if not curr.children:
                return False

            # If wildcard is used create a temporary node with merged children
            if word[i] == ".":
                merged_children = {}

                for key in curr.children:
                    merged_children |= curr.children[key].children

                temp_node = self.Node("", children=merged_children)
                curr = temp_node
                continue

            if word[i] not in curr.children:
                return False
            
            curr = curr.children[word[i]]
        
        # Handle the last character of word
        if word[-1] == ".":
            return any([curr.children[key].end_of_word for key in curr.children])
        
        return word[-1] in curr.children and curr.children[word[-1]].end_of_word
