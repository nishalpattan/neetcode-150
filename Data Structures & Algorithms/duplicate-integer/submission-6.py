class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = dict()
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for key, val in hash_map.items():
            if val > 1:
                return True
        return False