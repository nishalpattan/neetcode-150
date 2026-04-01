class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        for val in nums:
            hashMap[val] = 1 + hashMap.get(val, 0)
        for val in nums:
            if hashMap[val] > 1:
                return True
        return False