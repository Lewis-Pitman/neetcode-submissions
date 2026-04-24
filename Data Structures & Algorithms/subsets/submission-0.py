class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index: int, curr_path: List[int]) -> None:
            if index == len(nums):
                result.append(curr_path.copy())
                return

            # Keep current index
            curr_path.append(nums[index])
            backtrack(index + 1, curr_path)

            # Undo, and skip instead
            curr_path.pop()
            backtrack(index + 1, curr_path)

        backtrack(0, [])
        
        return result