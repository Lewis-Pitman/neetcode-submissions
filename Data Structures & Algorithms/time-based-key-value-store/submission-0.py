class TimeMap:
    """
    The TimeMap will store data like this:
    {
        "Key" : [(value, timestamp), (value, timestamp)]
    }

    Since timestamp always increases, the list of values is always
    sorted by timestamp, meaning we can binary search in the get method
    """

    def __init__(self):
        # If a key is set which doesn't exist, init with an empty list
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # e.g. If the first timestamp is 3, but user requests timestamp 2,
        # there is nothing before 2 and so we should return ""
        if not self.dic[key] or self.dic[key][0][1] > timestamp:
            return ""

        left = 0
        right = len(self.dic[key]) - 1

        while left <= right:
            middle = (left + right) // 2
            middleTimestamp = self.dic[key][middle][1]

            if middleTimestamp == timestamp:
                return self.dic[key][middle][0]
            
            if middleTimestamp > timestamp:
                right = middle - 1
            else:
                left = middle + 1
        
        return self.dic[key][right][0]





