class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top_index = stack.pop()
                height = heights[top_index]
                width = i if not stack else i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)

        # finalize remaining bars
        while stack:
            top_index = stack.pop()
            height = heights[top_index]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            area = max(area, height * width)

        return area
