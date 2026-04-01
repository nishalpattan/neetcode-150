class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # naive solution
         if len(nums) == 1 or len(nums) == 0:
            return False
         nums.sort()
         for idx, val in enumerate(nums):
            if idx != 0:
                if nums[idx] == nums[idx-1]:
                    return True
         return False
