from collections import defaultdict

class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        # Map to store the "hash" of the shifting pattern to the list of strings
        differenceMap = defaultdict(list)

        for string in strings:
            # A single character string can be represented by a constant pattern
            if len(string) == 0:
                differenceMap[()].append("")
                continue
            
            # Calculate the cyclic difference between adjacent characters
            # (ord(curr) - ord(prev)) % 26 ensures 'a' -> 'z' and 'z' -> 'a' logic
            differences = []
            for i in range(len(string) - 1):
                diff = (ord(string[i+1]) - ord(string[i])) % 26
                differences.append(diff)
            
            # Convert list to tuple so it can be used as a dictionary key
            differenceMap[tuple(differences)].append(string)
        
        return list(differenceMap.values())