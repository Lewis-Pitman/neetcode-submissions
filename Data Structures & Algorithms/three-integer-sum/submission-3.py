class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                tripletSum = nums[i] + nums[j] + nums[k]

                if tripletSum == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # skip duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif tripletSum > 0:
                    k -= 1
                else:
                    j += 1

        return result