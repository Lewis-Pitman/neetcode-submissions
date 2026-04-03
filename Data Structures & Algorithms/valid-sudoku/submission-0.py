class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(list)
        columnHash = defaultdict(list)

        # Ensure each row contains 1-9 without duplicates
        for index, row in enumerate(board):
            for cell in row:
                if cell == ".":
                    continue
                
                if cell in rowHash[index]:
                    return False
                
                rowHash[index].append(cell)
        
        # Ensure each column contains 1-9 without duplicates
        for column in range(0, 9):
            for row in board:
                cell = row[column]

                if cell == ".":
                    continue
                
                if cell in columnHash[column]:
                    return False
                
                columnHash[column].append(cell)

        # Ensure each 3x3 contains 1-9 without duplicates
        for subBox in range(0, 9):
            subBoxSet = set()

            rowOffset = (subBox // 3) * 3
            columnOffset = (subBox % 3) * 3

            for row in range(0, 3):
                for column in range(0, 3):
                    cell = board[row + rowOffset][column + columnOffset]

                    if cell == ".":
                        continue

                    if cell in subBoxSet:
                        return False
                    
                    subBoxSet.add(cell)

        return True