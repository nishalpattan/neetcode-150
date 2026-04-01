from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = list()
        res = list()
        print(freq_map.items())
        for val, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, val)) # what is time complexity of heappush
            if len(min_heap) > k:
                heapq.heappop(min_heap) # what is time complexity of heappop
        
        for freq, val in min_heap:
            res.append(val)
        
        return res
    