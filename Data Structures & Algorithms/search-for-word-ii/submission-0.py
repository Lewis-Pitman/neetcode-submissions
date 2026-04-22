class Solution:
    class Trie:
        class Node:
            def __init__(self, val: str) -> None:
                self.val = val
                self.children = {}
                self.word = False
                self.index = None

        def __init__(self) -> None:
            self.root = self.Node("")

        def insert(self, word: str, index: int) -> None:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = self.Node(char)
                curr = curr.children[char]
            curr.word = True
            curr.index = index

    def findWords(self, board, words):
        if not board:
            return []

        BOARD_WIDTH = len(board[0])
        BOARD_HEIGHT = len(board)

        trie = self.Trie()
        words_in_board = []

        # Initialise trie
        for index, word in enumerate(words):
            trie.insert(word, index)

        # Recursively check all possible paths from a cell
        def checkCell(pos, curr_node, used_cells):
            if pos in used_cells:
                return

            col, row = pos

            if board[row][col] not in curr_node.children:
                return

            used_cells = used_cells.copy()
            used_cells.add(pos)

            curr_node = curr_node.children[board[row][col]]

            if curr_node.word:
                words_in_board.append(words[curr_node.index])
                curr_node.word = False  # avoid duplicates

            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in directions:
                new_col = col + dx
                new_row = row + dy

                if 0 <= new_col < BOARD_WIDTH and 0 <= new_row < BOARD_HEIGHT:
                    checkCell((new_col, new_row), curr_node, used_cells)

        # Iterate through every cell
        for row in range(BOARD_HEIGHT):
            for col in range(BOARD_WIDTH):
                checkCell((col, row), trie.root, set())

        return words_in_board