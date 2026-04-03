class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return

        rotateAmount = k % len(nums)

        left = 0
        right = (len(nums) - 1) - (rotateAmount - 1)

        while right != len(nums):
            leftStorage = nums[left]
            leftStartIndex = left
            
            nums[left] = nums[right]

            left += 1
            
            while left <= right:
                leftStorage, nums[left] = nums[left], leftStorage
                left += 1
            
            left = leftStartIndex + 1
            right += 1


        