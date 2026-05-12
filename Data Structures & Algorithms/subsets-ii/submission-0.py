class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        nums_len = len(nums) - 1

        def backtrack(curr_subset: List[int], curr_index) -> None:
            # If we have used all available numbers
            if curr_index > nums_len:
                result.append(curr_subset.copy())
                return

            # Take the current index
            curr_subset.append(nums[curr_index])
            backtrack(curr_subset, curr_index + 1)

            # Backtrack and don't take current index
            curr_subset.pop()

            # Avoid duplicates
            while curr_index + 1 < len(nums) and nums[curr_index] == nums[curr_index + 1]:
                curr_index += 1

            backtrack(curr_subset, curr_index + 1)

        backtrack([], 0)

        return result