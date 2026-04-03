class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_row_length = len(matrix)

        # Find which row the target will be in
        row = 0

        while row < matrix_row_length and matrix[row][0] <= target:
            row += 1

        row -= 1

        # Perform binary search on this row
        start_index = 0
        end_index = len(matrix[row]) - 1

        while start_index <= end_index:
            middle_index = start_index + ((end_index - start_index) // 2)

            if matrix[row][middle_index] == target:
                return True
            elif matrix[row][middle_index] > target:
                end_index = middle_index - 1
            else:
                start_index = middle_index + 1
        
        return False