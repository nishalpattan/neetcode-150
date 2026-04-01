class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        
        for num in nums:
            if hashMap[num] > 1:
                return True

        return False