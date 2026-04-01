from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = list()
        # res = list()
        # print(freq_map.items())
        # for val, freq in freq_map.items():
        #     heapq.heappush(min_heap, (freq, val)) # what is time complexity of heappush
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap) # what is time complexity of heappop
        
        # for freq, val in min_heap:
        #     res.append(val)
        
        # return res

        # Bucket sort : TC : O(n), SC: O(n)
        # 1. build freq/count map
        # 2. initialize list of lists of size (n+1)
        # 3. iterate through the freq map and store the value at freq index
        # 4. as the list of lists is from 0 to n+1 index, reverse iterate and collect values from each index bucket,\
            # store in output resuls as once the size reaches k return the result
        
        freq_map = Counter(nums)
        bucket_list = [[] for _ in range(len(nums)+1)]
        res = list()

        for val, freq in freq_map.items():
            bucket_list[freq].append(val)
        
        for idx in range(len(bucket_list)-1, -1, -1):
            for val in bucket_list[idx]:
                res.append(val)
                if len(res) == k:
                    return res
        return res

    