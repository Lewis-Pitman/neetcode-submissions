class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            sum = numbers[right] + numbers[left]

            if sum == target:
                break
            else:
                if sum > target:
                    right -= 1
                else:
                    left += 1
        
        return [left + 1, right + 1]
            