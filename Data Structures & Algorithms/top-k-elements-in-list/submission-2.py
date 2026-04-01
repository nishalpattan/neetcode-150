class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # approach: use frequency counter 
        # TC: O(n logn), SC : O(n)
        # hashMap = defaultdict(int)
        # result = list()

        # for num in nums:
        #     hashMap[num] += 1
        
        # hashMap = dict(sorted(hashMap.items(), key = lambda item : item[1], reverse=True))
        # result = list(hashMap.keys())[:k]
        # return result
        
        #  using heap, TC : O(n log k), SC:O(n)
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1

        min_heap = []
        result = list()
        for num, freq in hashMap.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])
        return result
        

