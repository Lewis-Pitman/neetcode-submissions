class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numberOfColumns = len(matrix[0])
        numberOfRows = len(matrix)
        size = numberOfColumns * numberOfRows
        startIndex = 0
        endIndex = size - 1

        while startIndex <= endIndex:
            middleIndex = (startIndex + endIndex) // 2

            middleRow = middleIndex // numberOfColumns
            middleColumn = middleIndex % numberOfColumns

            middleCell = matrix[middleRow][middleColumn]

            if middleCell == target:
                return True
            elif middleCell > target:
                endIndex = middleIndex - 1
            else:
                startIndex = middleIndex + 1
        
        return False