class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]

        hashMap = defaultdict(int)

        for idx, val in enumerate(nums):

            if target - val in hashMap:
                return [hashMap[target - val], idx]
            
            hashMap[val] = idx
        return [-1,-1]

