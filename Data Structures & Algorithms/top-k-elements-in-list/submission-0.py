class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        sorted_data_desc = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        
        keys_list = list(sorted_data_desc.keys())
        return keys_list[:k]