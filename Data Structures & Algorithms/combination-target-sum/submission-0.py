class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, curr_path, curr_sum):
            if curr_sum == target:
                result.append(curr_path.copy())
                return

            if curr_sum > target or index == len(nums):
                return

            # Take current number (Can be done multiple times in a row)
            curr_path.append(nums[index])
            backtrack(index, curr_path, curr_sum + nums[index])

            # Undo choice
            curr_path.pop()

            # Skip current number
            backtrack(index + 1, curr_path, curr_sum)

        backtrack(0, [], 0)
        return result