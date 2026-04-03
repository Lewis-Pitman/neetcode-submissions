class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            j = len(numbers) - 1

            while j >= 0:
                if j != i and numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                
                j -= 1