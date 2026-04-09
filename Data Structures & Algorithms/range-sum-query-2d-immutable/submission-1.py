class NumMatrix:
    # Solution using the prefix sum method featured in
    # the solution video
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
            
        rows, cols = len(matrix), len(matrix[0])
        # Create a matrix padded with an extra row and column of 0s
        # (Algorithm needs to always add above cell and left cell, even
        # if the region we want to sum is on the left/top edge)
        self.prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                original_cell_value = matrix[row - 1][col - 1]
                sum_above = self.prefix_sum[row - 1][col]
                sum_left = self.prefix_sum[row][col - 1]
                region_counted_twice = self.prefix_sum[row - 1][col - 1]

                prefix_sum = ((original_cell_value + sum_above
                + sum_left) - region_counted_twice)

                self.prefix_sum[row][col] = prefix_sum


    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # We use +1 on all indices because of our padding
        bottom_right_sum = self.prefix_sum[r2 + 1][c2 + 1]
        above_sum = self.prefix_sum[r1][c2 + 1]
        left_sum = self.prefix_sum[r2 + 1][c1]
        double_counted_region = self.prefix_sum[r1][c1]

        return ((bottom_right_sum - above_sum - left_sum)
        + double_counted_region)
        