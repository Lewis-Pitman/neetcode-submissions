class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        best = 0

        start = 0

        for i in range(len(s)):
            while s[i] in seen_chars:
                seen_chars.remove(s[start])
                start += 1
                
            seen_chars.add(s[i])
                
            best = max(best, (i-start) + 1)

        return best
