import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitised = s.lower()
        sanitised = "".join(
            char for char in sanitised
            if char not in string.punctuation and not char.isspace()
        )
        
        return sanitised == sanitised[::-1]
