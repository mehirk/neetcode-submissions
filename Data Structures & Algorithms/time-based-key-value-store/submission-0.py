from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        left = 0
        right = len(pairs) - 1
        ans = ""

        while left <= right:
            mid = left + (right - left) // 2

            mid_value = pairs[mid][0]
            mid_timestamp = pairs[mid][1]

            if mid_timestamp == timestamp:
                return mid_value
            elif mid_timestamp > timestamp:
                right = mid - 1
            else:
                ans = mid_value
                left = mid + 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)