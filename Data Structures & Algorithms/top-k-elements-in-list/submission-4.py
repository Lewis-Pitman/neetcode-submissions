class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)

        for num in nums:
            numCount[num] = numCount[num] + 1

        # Most frequent numbers in descending order
        mostFrequent = []

        for num, count in zip(numCount.keys(), numCount.values()):
            mostFrequent.append([count, num])
        
        mostFrequent.sort()

        final = []

        for i in range(1, k + 1):
            final.append(mostFrequent[-i][1])

        return final

        