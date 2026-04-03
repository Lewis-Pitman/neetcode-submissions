class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Construct hashmap of the number of occurrences of each character
        # for both strings
        sCharOccurrences = {}

        for char in s:
            if char in sCharOccurrences:
                sCharOccurrences[char] = sCharOccurrences[char] + 1
            else:
                sCharOccurrences[char] = 1

        tCharOccurrences = {}

        for char in t:
            if char in tCharOccurrences:
                tCharOccurrences[char] = tCharOccurrences[char] + 1
            else:
                tCharOccurrences[char] = 1

        # Iterate of s keys and check t both has that letter
        # and has the same no. of occurrences

        for char in sCharOccurrences.keys():
            if char not in tCharOccurrences:
                return False

            if tCharOccurrences[char] != sCharOccurrences[char]:
                return False

        return True