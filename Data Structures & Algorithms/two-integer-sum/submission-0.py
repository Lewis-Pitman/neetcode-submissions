class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], index]
            else:
                seen[num] = index
        
        return []