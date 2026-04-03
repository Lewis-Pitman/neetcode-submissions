# Help from solution tab

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict assigns a value to keys not existing
        # This means you don't need to check yourself
        res = defaultdict(list)

        for s in strs:
            # sorted() returns a list so needs to be joined together
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
            
        return list(res.values())