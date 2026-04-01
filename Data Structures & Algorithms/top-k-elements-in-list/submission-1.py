class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = defaultdict(int)
        result = list()

        for num in nums:
            hashMap[num] += 1
        
        hashMap = dict(sorted(hashMap.items(), key = lambda item : item[1], reverse=True))
        result = list(hashMap.keys())[:k]
        return result