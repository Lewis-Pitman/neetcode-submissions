class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        sortedNums = sorted(nums)
        longestLength = 1
        currentLength = 1

        for i in range(1, len(nums)):
            if sortedNums[i-1] + 1 == sortedNums[i]:
                currentLength += 1
            elif  sortedNums[i-1] == sortedNums[i]:
                pass
            else:
                if currentLength > longestLength:
                    longestLength = currentLength
                
                currentLength = 1
        
        return max(longestLength, currentLength)
