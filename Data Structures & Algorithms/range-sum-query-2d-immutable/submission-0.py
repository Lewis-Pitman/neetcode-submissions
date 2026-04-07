# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

from itertools import chain

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Flatten the list of lists
        self.matrix = list(chain.from_iterable(matrix))
        self.row_length = len(matrix[0])
        self.col_length = len(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_width = col2 - col1
        region_height = row2 - row1
        region_sum = 0

        curr_row = row1
        while curr_row <= row2:
            start_ptr = (curr_row * self.row_length) + col1
            region_sum += self.matrix[start_ptr]

            for i in range(region_width):
                region_sum += self.matrix[start_ptr + i + 1]

            curr_row += 1

        return region_sum
