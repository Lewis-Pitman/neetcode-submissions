class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k Will start at the biggest pile
        startIndex = 1
        endIndex = max(piles)

        while startIndex <= endIndex:
            k = (startIndex + endIndex) // 2

            # Calculate hours taken
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k
            
            if hours > h:
                startIndex = k + 1
            else:
                endIndex = k - 1
        
        return startIndex

