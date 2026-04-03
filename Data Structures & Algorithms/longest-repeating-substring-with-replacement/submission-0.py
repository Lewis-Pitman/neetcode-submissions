from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_f = 0
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1
            # Track the frequency of the most common character in the current window
            max_f = max(max_f, count[s[right]])

            # Current window size is (right - left + 1)
            # Characters to replace = (window size) - (most frequent character count)
            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
            
            # Update the result with the maximum valid window found
            res = max(res, right - left + 1)

        return res