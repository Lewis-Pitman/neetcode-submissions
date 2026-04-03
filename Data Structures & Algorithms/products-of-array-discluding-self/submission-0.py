class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndexes = []

        for index, num in enumerate(nums):
            if num == 0:
                zeroIndexes.append(index)

        if len(zeroIndexes) >= 2:
            return [0] * len(nums)
        elif len(zeroIndexes) == 1:
            numsProduct = 1

            for i in range(0, zeroIndexes[0]):
                numsProduct = numsProduct * nums[i]

            for j in range(zeroIndexes[0] + 1, len(nums)):
                numsProduct = numsProduct * nums[j]
            
            result = [0] * len(nums)
            result[zeroIndexes[0]] = numsProduct
            return result
        else:

            numsProduct = 1

            for num in nums:
                numsProduct = numsProduct * num
        
            return [numsProduct // num for num in nums]